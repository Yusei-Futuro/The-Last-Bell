from tkinter.font import names

from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Username, Situations, History_Choice, NPCRelationship
#Falta obligatoriamente el GameSave() importarlo aca

# Create your views here.

@login_required()
def main_game(request):

    #Esta parte del codigo esta establecida para el desarrollo del menu del game con las opciones
    #Continuar partida si existe, cargar partida, resultados,salir

    player_profile=request.user.username
    #Buscame la parte de guardar partida

    context = {
        'player_profile': player_profile,
        #Tengo aca que buscar el ultimo guardado
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

    #Aca hay que poner GameSave pero la parte del juego seria eliminada el progreso anterior

    return redirect("prologue")

@login_required
def prologue(request): #Aca esta la parte del prologo del juego
    return HttpResponse("Hello word")

@login_required
def load_game(request):#Aca va el load game del juego
    return HttpResponse("Hello word")

@login_required
def play_situations(request, situation_id):

    user=request.user.Username
    situation=get_object_or_404(Situations, id=situation_id)

    dialogue=situation.dialogue.all().orden.by("orden")
    current_line_index = request.session.get(f'situation_{situation_id}_line', 0)

    if current_line_index >= dialogue.count():

        return redirect('situation_complete', situation_id=situation_id)

    current_line = dialogue[current_line_index]
    # Si es punto de decisión, mostrar opciones
    if current_line.is_decision_point:
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
    choice = get_object_or_404(Username, id=choice_id)
    situation = choice.dialogue.situation
    npc = situation.main_character
    relationship, created = NPCRelationship.objects.get_or_create(
        player=player_profile,
        character=npc
    )
    relationship.update_friendship(choice.friendship_points)
    History_Choice.objects.create(
        player=player_profile,
        choice=choice,
        situation=situation,
        day=player_profile.current_day,
        points_earned=choice.friendship_points
    )

    player_profile.total_friendship_score += choice.friendship_points
    player_profile.save()

    # Crear autosave

    if choice.next_dialogue:
        next_index = choice.next_dialogue.order
        request.session[f'situation_{situation.id}_line'] = next_index

    return redirect('play_situation', situation_id=situation.id)

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

#Me faltan aca otras view que tengo planeadas situation_complete, game_complete, continue_next_day


