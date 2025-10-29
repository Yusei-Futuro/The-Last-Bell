from django.shortcuts import render , redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.management.base import BaseCommand
from .models import Character, Location, Situations, Dialogue, Choice

# Create your views here.

@login_required()
def main_game(request):
    return render(request,"main game.html")

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

#Parte de pablo sobre el game

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

class Command(BaseCommand):
    help = 'Carga el contenido del Día 1 desde dialogos.txt'

    def handle(self, *args, **kwargs):
        # Crear personajes
        self.create_characters()

        # Crear locaciones
        self.create_locations()

        # Crear situaciones
        self.create_situations()

        # Crear diálogos
        self.create_dialogues()

        self.stdout.write(self.style.SUCCESS('Contenido del Día 1 cargado exitosamente!'))

    def create_characters(self):
        # Álex
        Character.objects.get_or_create(
            name="Álex",
            defaults={
                'backstory': 'Compañero nuevo que saluda antes de entrar a clase',
                'interests': 'Socializar',
                'personality': 'Amigable y abierto',
                'friendship_threshold': 20
            }
        )