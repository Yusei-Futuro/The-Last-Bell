from tkinter.font import names

from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Username, Situations, History_Choice, NPCRelationship, Choice, GameSave

# Create your views here.

def main(request):
    return render(request, "main_base.html")

def sign(request):
    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],
                                                password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("main_player")
            except:
                return render(request, "signup.html",{
                    "form": UserCreationForm(),
                    "Error": "User already exist"
                })

        return render(request,"signup.html",{
            "Form":UserCreationForm(),
            "Error": "Password not same"
        })

def logo_out(request):
    logout(request)
    return redirect("main_player")

def singin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm()
        })
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])

        if user == None:
            return render(request, "signin.html", {
                "form": AuthenticationForm(),
                "Error": "Error en la contraseña o el usuario pruebe otra vez"
            })

        else:
            login(request, user)
            return redirect("main_game")

@login_required()
def main_game(request):

    #Esta parte del codigo esta establecida para el desarrollo del menu del game con las opciones
    #Continuar partida si existe, cargar partida, resultados,salir

    player_profile=request.user.Username
    latest_save = GameSave.objects.filter(player=player_profile).first()

    context = {
        'player_profile': player_profile,
        'has_saved_game': latest_save is not None,
        'latest_save': latest_save,
    }

    return render(request,"game/main game.html", context)

@login_required
def new_game(request):

    #Funcion que reinicia los ajustes a predeterminados
    user=request.user.Username

    user.day = 1
    user.situation_complet = False
    user.friend = 0
    user.friends_count = 0
    user.game_completed = False
    user.save()

    GameSave.objects.filter(player=user).delete()

    return redirect("play_situation", situation_id=1)

@login_required
def prologue(request): #Aca esta la parte del prologo del juego
    return HttpResponse("Hello word")

@login_required
def load_game(request):#Aca va el load game del juego

    player_profile = request.user.Username
    latest_save = GameSave.objects.filter(player=player_profile).first()

    if not latest_save:
        return redirect('new_game')

    return redirect('play_situation', situation_id=latest_save.current_situation.id)

@login_required
def play_situations(request, situation_id):

    player_profile = request.user.Username
    situation = get_object_or_404(Situations, id=situation_id)

    dialogue = situation.dialogue_lines.all().order_by("order")
    current_line_index = request.session.get(f'situation_{situation_id}_line', 0)

    if current_line_index >= dialogue.count():
        return redirect('situation_complete', situation_id=situation_id)

    current_line = dialogue[current_line_index]

    if current_line.decision_point:
        choices = current_line.choices.all().order_by('order')
        context = {
            'situation': situation,
            'dialogue_line': current_line,
            'choices': choices,
            'is_decision_point': True,
        }
        return render(request, 'game/situation.html', context)

    context = {
        'situation': situation,
        'dialogue_line': current_line,
        'is_decision_point': False,
    }

    request.session[f'situation_{situation_id}_line'] = current_line_index + 1

    return render(request, 'game/situation.html', context)

@login_required
def make_choice(request, choice_id):
    if request.method != 'POST':
        return redirect('main_menu')

    player_profile = request.user.Username
    choice = get_object_or_404(Choice, id=choice_id)
    situation = choice.dialogue.situation
    npc = situation.character
    relationship, created = NPCRelationship.objects.get_or_create(
        player=player_profile,
        character=npc
    )
    relationship.update_friendship(choice.friendship_points)


    History_Choice.objects.create(
        player=player_profile,
        choice=choice,
        situation=situation,
        day=player_profile.day,
        points_earned=choice.friendship_points
    )

    player_profile.friend += choice.friendship_points
    player_profile.save()

    GameSave.create_autosave(
        player_profile=player_profile,
        situation=situation,
        dialogue_line=choice.next_dialogue or choice.dialogue
    )

    if choice.next_dialogue:
        next_index = choice.next_dialogue.order
        request.session[f'situation_{situation.id}_line'] = next_index
    else:
        request.session[f'situation_{situation.id}_line'] += 1

    return redirect('play_situation', situation_id=situation.id)

@login_required
def continue_to_next_day(request):
    player_profile = request.user.Username

    player_profile.advance_to_next_day()
    next_situation = Situations.objects.filter(day=player_profile.day).first()

    if next_situation:
        return redirect('play_situation', situation_id=next_situation.id)
    else:
        return redirect('game_complete')

@login_required
def game_complete(request):
    player_profile = request.user.Username
    friends_count = player_profile.calculate_friends()

    relationships = player_profile.npc_relationships.all().order_by('-friendship_points')

    player_profile.final= True
    player_profile.save()

    context = {
        'player_profile': player_profile,
        'friends_count': friends_count,
        'relationships': relationships,
        'total_days': 7,
    }
    return render(request, 'game/game_complete.html', context)

@login_required
def situation_complete(request, situation_id):

    player_profile = request.user.Username
    situation = get_object_or_404(Situations, id=situation_id)

    player_profile.current_situation_completed = True
    player_profile.save()

    request.session.pop(f'situation_{situation_id}_line', None)

    current_friends = player_profile.calculate_friends()
    if player_profile.day >= 7:
        return redirect('game_complete')

    next_day = player_profile.day + 1
    next_situation = Situations.objects.filter(day=next_day).first()

    context = {
        'situation': situation,
        'next_situation': next_situation,
        'current_day': player_profile.day,
        'current_friends': current_friends,
    }

    return render(request, 'game/situation_complete.html', context)