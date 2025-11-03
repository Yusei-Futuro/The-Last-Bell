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

    # Buscar la primera situación del día 1 dinámicamente
    first_situation = Situations.objects.filter(day=1).first()
    if not first_situation:
        # Si no hay situación para el día 1, redirigir al menú principal
        return redirect("main_game")

    return redirect("play_situation", situation_id=first_situation.id)

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

    # Obtener el ID del diálogo actual desde la sesión
    current_dialogue_id = request.session.get(f'situation_{situation_id}_dialogue_id', None)
    branch_start_order = request.session.get(f'situation_{situation_id}_branch_start', None)

    # Si no hay diálogo actual, empezar con el primero de la situación
    if current_dialogue_id is None:
        # Obtener el primer diálogo (order más bajo)
        current_line = situation.dialogue_lines.order_by('order').first()
        if not current_line:
            return redirect('situation_complete', situation_id=situation_id)
    else:
        # Obtener el diálogo actual por ID
        from .models import Dialogue
        try:
            current_line = Dialogue.objects.get(id=current_dialogue_id, situation=situation)
        except Dialogue.DoesNotExist:
            return redirect('situation_complete', situation_id=situation_id)

    # Si es un punto de decisión, mostrar las opciones
    if current_line.decision_point:
        choices = current_line.choices.all().order_by('order')
        context = {
            'situation': situation,
            'dialogue_line': current_line,
            'choices': choices,
            'is_decision_point': True,
        }
        return render(request, 'game/situation.html', context)

    # Calcular el siguiente diálogo para el botón "Continuar"
    next_dialogue = _get_next_dialogue(current_line, situation, branch_start_order)

    if next_dialogue:
        # Guardar el ID del siguiente diálogo en la sesión
        request.session[f'situation_{situation_id}_dialogue_id'] = next_dialogue.id
        is_last_dialogue = False
    else:
        # No hay más diálogos, limpiar la sesión
        request.session[f'situation_{situation_id}_dialogue_id'] = None
        is_last_dialogue = True

    context = {
        'situation': situation,
        'dialogue_line': current_line,
        'is_decision_point': False,
        'is_last_dialogue': is_last_dialogue,
    }

    return render(request, 'game/situation.html', context)


def _get_next_dialogue(current_dialogue, situation, branch_start_order=None):
    """
    Determina el siguiente diálogo en la secuencia.

    - Si estamos en una rama específica (branch_start_order no es None),
      solo acepta diálogos EXACTAMENTE consecutivos (order + 1)
    - Cualquier salto (incluso de 1) después de una decisión termina la rama
    - Busca el siguiente diálogo por order
    """
    # Buscar el siguiente diálogo inmediato por order
    next_dialogue = situation.dialogue_lines.filter(
        order__gt=current_dialogue.order
    ).order_by('order').first()

    if not next_dialogue:
        return None

    # Si estamos en una rama específica (después de una decisión)
    if branch_start_order is not None:
        # Verificar que el siguiente diálogo sea EXACTAMENTE consecutivo
        # Esto evita saltar a otra rama
        if next_dialogue.order != current_dialogue.order + 1:
            # No es consecutivo, fin de la rama
            return None

    return next_dialogue

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

    player_profile.friend_counts += choice.friendship_points
    player_profile.save()

    # Determinar el siguiente diálogo
    if choice.next_dialogue:
        next_dialogue = choice.next_dialogue
        # Guardar el ID del siguiente diálogo
        request.session[f'situation_{situation.id}_dialogue_id'] = next_dialogue.id
        # Guardar el order de inicio de la rama para filtrar correctamente
        request.session[f'situation_{situation.id}_branch_start'] = next_dialogue.order
    else:
        # Si no hay next_dialogue definido, avanzar al siguiente por order
        next_dialogue = _get_next_dialogue(choice.dialogue, situation, None)
        if next_dialogue:
            request.session[f'situation_{situation.id}_dialogue_id'] = next_dialogue.id
        else:
            request.session[f'situation_{situation.id}_dialogue_id'] = None

    GameSave.create_autosave(
        player_profile=player_profile,
        situation=situation,
        dialogue_line=next_dialogue or choice.dialogue
    )

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

    player_profile.situation_complet = True
    player_profile.save()

    # Limpiar las variables de sesión de la situación
    request.session.pop(f'situation_{situation_id}_dialogue_id', None)
    request.session.pop(f'situation_{situation_id}_branch_start', None)
    # Mantener compatibilidad con el sistema antiguo
    request.session.pop(f'situation_{situation_id}_line', None)

    current_friends = player_profile.calculate_friends()
    if player_profile.day >= 7:
        return redirect('game_complete')

    next_day = player_profile.day + 1
    next_situation = Situations.objects.filter(day=next_day).first()
    player_profile.day = next_day
    player_profile.save()

    # Crear un autosave apuntando al inicio del siguiente día
    if next_situation:
        first_dialogue = next_situation.dialogue_lines.order_by('order').first()
        GameSave.create_autosave(
            player_profile=player_profile,
            situation=next_situation,
            dialogue_line=first_dialogue
        )

    context = {
        'situation': situation,
        'next_situation': next_situation,
        'current_day': player_profile.day,
        'current_friends': current_friends,
    }

    return render(request, 'game/situation_complete.html', context)