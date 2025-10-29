from tkinter.font import names

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
        #Kove
        Character.objects.get_or_create(
            name="Kove",
            defaults={
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "trait": "Reservado, curioso",
                "interesting": "Le encanta leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20
            }
        )
        #Mama
        Character.objects.get_or_create(
            name="Mamá",
            defaults={
                "backstory": "Madre de Kove, trabaja mucho y se preocupa por su hijo",
                "trait": "Protector, estricto",
                "interesting": "Le gusta mantener todo organizado",
                "personality": "Cariñosa pero estricta",
                "is_friend": 0
            }
        )
        #Bibliotecario Zu
        Character.objects.get_or_create(
            name="Bibliotecario Zu",
            defaults={
                "backstory": "Ama los libros y disfruta compartir su conocimiento",
                "trait": "Reservado, amable",
                "interesting": "Le gusta leer y recomendar libros",
                "personality": "Paciente y observador",
                "is_friend": 20
            }
        )
        #Brad
        Character.objects.get_or_create(
            name="Brad",
            defaults={
                "backstory": "Ama jugar al futbool",
                "trait": "Energetico, amable",
                "interesting": "Le gusta jugar a la pelota y generalmente molestar",
                "personality": "Egocentrico pero pacifico",
                "is_friend": 20
            }
        )
        #Isabella
        Character.objects.get_or_create(
            name="Isabella",
            defaults={
                "backstory": "Ama pintar mucho y varias veces la fotografia",
                "trait": "Energetica, amable, divertida",
                "interesting": "Le gusta pintar mucho y pasar tiempo asolas",
                "personality": "Divertida, pacifica, tranquila y amable",
                "is_friend": 20
            }
        )
        #Sandro
        Character.objects.get_or_create(
            name="Sandro",
            defaults={
                "backstory": "Ama jugar Ajedrez por las noches se diria que sueña con el",
                "trait": "Energetica, amable, egocentrico, honrado, valiente",
                "interesting": "Le gusta mantenerse brillante como sus movimientos en ajedrez",
                "personality": "Divertido, pacifico, tranquilo y amable",
                "is_friend": 20
            }
        )
        #Pedro
        Character.objects.get_or_create(
            name="Pedro",
            defaults={
                "backstory": "Es bastante atletico",
                "trait": "Energetico",
                "interesting": "Le gusta hacer muchos deportes",
                "personality": "Energetica y fuerte",
                "is_friend": 20
            }
        )
        #Estafany
        Character.objects.get_or_create(
            name="Estefany",
            defaults={
                "backstory": "Risueña y divertida pero muy seria para el estudio",
                "trait": "Risueña",
                "interesting": "Le gusta estudiar se la pasa en la parte de estudio",
                "personality": "Estudiar y bailar",
                "is_friend": 20
            }
        )
        #Victor Joe
        Character.objects.get_or_create(
            name="Victor Joe",
            defaults={
                "backstory": "Es entrometido pero le encanta la musica",
                "trait": "Le gusta mucho la musica",
                "interesting": "Le gusta la musica y perderse en los libros y la musica",
                "personality": "Es amigable y socialmente agradable",
                "is_friend": 20
            }
        )

def create_situation_1_biblioteca(self):
    # Obtener personaje y locación
    bibliotecario = Character.objects.get(name="Bibliotecario")
    biblioteca = Location.objects.get(name="Biblioteca Central")

    # Crear situación del Día 1
    situation = Situations.objects.create(
        day=1,  # Día 1 = Situación 1
        title="Conflicto por el libro",
        location=biblioteca,
        main_character=bibliotecario,
        context="Came busca un libro de fantasía pero alguien más lo quiere también"
    )

    # Línea 1: Narración
    line1 = Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Mmmm parece ser la biblioteca central de la escuela, no es un mal lugar para pasar el tiempo...",
        order=1,
        is_decision_point=False
    )

    # Línea 2: Pensamiento de Came
    line2 = Dialogue.objects.create(
        situation=situation,
        line_type='came_thought',
        text="me pregunto si tendrán la nueva edición de (nombre_libro)",
        order=2,
        is_decision_point=False
    )

    # ... continuar con todas las líneas

    # Punto de decisión
    decision_line = Dialogue.objects.create(
        situation=situation,
        character=bibliotecario,
        line_type='npc_speech',
        text="Disculpa mis modales, me llamo (name) y me gusta leer...",
        order=10,
        is_decision_point=True
    )

    # Opción 1: Buena
    choice1 = Choice.objects.create(
        dialogue_line=decision_line,
        choice_text="Aceptar las disculpas de (name bibliotecario)",
        consequence_text="Sí lo siento también es mi culpa por actuar así...",
        friendship_points=10,
        choice_type='buena',
        order=1
    )

    # Opción 2: Mala
    choice2 = Choice.objects.create(
        dialogue_line=decision_line,
        choice_text="Ignorar las disculpas de (name bibliotecario)",
        consequence_text="No las acepto pareces una mala persona",
        friendship_points=-5,
        choice_type='mala',
        order=2
    )

