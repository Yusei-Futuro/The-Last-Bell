from tkinter.font import names

from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Username, Situations
#Falta obligatoriamente el GameSave() importarlo aca

# Create your views here.

@login_required()
def main_game(request):

    #Esta parte del codigo esta establecida para el desarrollo del menu del game con las opciones
    #Continuar partida si existe, cargar partida, resultados,salir

    user=request.user.Username
    #Buscame la parte de guardar partida

    context = {
        'player_profile': user,
        #Tengo aca que buscar el ultimo guardado
    }

    return render(request,"main game.html", context)

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
            return redirect("/main/")

def dialogue_view(request, dialogue_id):
    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)
    choices = dialogue.choices.all() if dialogue.decision_point else []
    return render(request, 'game.html', {
        'dialogue': dialogue,
        'choices': choices
    })

def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)

    # Actualizar puntos de amistad
    request.session['friendship'] = request.session.get('friendship', 0)
    request.session['friendship'] += choice.friendship_points

    # Ir al siguiente diálogo automáticamente
    if choice.next_dialogue:
        return redirect('dialogue_view', dialogue_id=choice.next_dialogue.id)
    else:
        # Si no hay siguiente diálogo, ir al menú principal
        return redirect('main')  # Aquí 'main' es tu ruta del menú principal


