from django.shortcuts import render , redirect, get_object_or_404
from .models import Username, Dialogue, Choice
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

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





#mando nivel 1
from TBL.models import Character, Situations, Dialogue, Choice

# --- Crear/obtener personajes ---
kove, created = Character.objects.get_or_create(
    name="Kove",
    defaults={
        "backstory":"Se mudó a una nueva ciudad recientemente...",
        "trait":"Reservado, curioso",
        "interesting":"Le encanta leer y conocer nuevos lugares",
        "personality":"Amable, un poco tímido",
        "is_friend":20
    }
)

mama, _ = Character.objects.get_or_create(
    name="Mamá",
    defaults={
        "backstory":"Madre de Kove, trabaja mucho y se preocupa por su hijo",
        "trait":"Protector, estricto",
        "interesting":"Le gusta mantener todo organizado",
        "personality":"Cariñosa pero estricta",
        "is_friend":0
    }
)

alex, _ = Character.objects.get_or_create(
    name="Alex",
    defaults={
        "backstory":"Compañero de clase nuevo, amigable y extrovertido",
        "trait":"Sociable",
        "interesting":"Le gusta hacer nuevos amigos",
        "personality":"Divertido y simpático",
        "is_friend":15
    }
)

bibliotecario, _ = Character.objects.get_or_create(
    name="Bibliotecario",
    defaults={
        "backstory":"Ama los libros y disfruta compartir su conocimiento",
        "trait":"Reservado, amable",
        "interesting":"Le gusta leer y recomendar libros",
        "personality":"Paciente y observador",
        "is_friend":20
    }
)

# --- Crear situación Día 1 ---
situacion_day1, _ = Situations.objects.get_or_create(
    day=1,
    defaults={
        "title":"Primer día de escuela",
        "locations": None,
        "contexto_situation":"Llegada a la escuela y primeras interacciones",
        "is_gameplay": True,
        "orden_dialogue": 0
    }
)

# --- Crear diálogos ---
d1, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=1,
    defaults={
        "character": mama,
        "text": "¡Hijo! Vamos tarde a tu primer día de escuela, termina de comer rápido",
        "decision_point": False,
        "lines_type": "npc_speech"
    }
)

d2, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=2,
    defaults={
        "character": kove,
        "text": "Perdón Mamá, terminé de comer altiro",
        "decision_point": False,
        "lines_type": "came_speech"
    }
)

d3, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=3,
    defaults={
        "character": mama,
        "text": "¡No olvides tu mochila!",
        "decision_point": False,
        "lines_type": "npc_speech"
    }
)

d4, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=4,
    defaults={
        "character": kove,
        "text": "Sí Mamá",
        "decision_point": False,
        "lines_type": "came_speech"
    }
)

d5, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=5,
    defaults={
        "character": None,
        "text": "Kove sale corriendo por la puerta",
        "decision_point": False,
        "lines_type": "came_thought"
    }
)

d6, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=6,
    defaults={
        "character": kove,
        "text": "Mmmm parece ser la biblioteca central de la escuela, no es un mal lugar para pasar el tiempo...",
        "decision_point": False,
        "lines_type": "came_thought"
    }
)

d7, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=7,
    defaults={
        "character": kove,
        "text": "Lo tengo, es mío por fin",
        "decision_point": False,
        "lines_type": "came_speech"
    }
)

d8, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=8,
    defaults={
        "character": bibliotecario,
        "text": "¿Quién eres y por qué tocas mi libro?",
        "decision_point": True,
        "lines_type": "npc_speech"
    }
)

# --- Crear opciones de decisión ---
# Decisión 1: Ignorar disculpas
d9, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=9,
    defaults={
        "character": None,
        "text": "A Kove le duelen esas palabras",
        "decision_point": False,
        "lines_type": "came_thought"
    }
)

c1, _ = Choice.objects.get_or_create(
    dialogue=d8,
    order=1,
    defaults={
        "text_choice": "No acepto tus disculpas, parece que eres una mala persona",
        "consequence": "Kove se va enojado y herido por las palabras del bibliotecario.",
        "next_dialogue": d9,
        "type_choice": "neutral",
        "friendship_points": -5
    }
)

# Decisión 2: Aceptar disculpas
d10, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=10,
    defaults={
        "character": bibliotecario,
        "text": "Ok Kove, parece que te gusta mucho leer...",
        "decision_point": False,
        "lines_type": "npc_speech"
    }
)

c2, _ = Choice.objects.get_or_create(
    dialogue=d8,
    order=2,
    defaults={
        "text_choice": "Está bien, lo entiendo, disculpa también, mi nombre es Kove",
        "consequence": "Kove inicia una nueva amistad con el bibliotecario",
        "next_dialogue": d10,
        "type_choice": "neutral",
        "friendship_points": 10
    }
)

# Continuación del diálogo de la decisión 2
d11, _ = Dialogue.objects.get_or_create(
    situation=situacion_day1,
    orden=11,
    defaults={
        "character": kove,
        "text": "¡Siii me encanta! Mi historia favorita es ...",
        "decision_point": False,
        "lines_type": "came_speech"
    }
)

# Asegurar que la segunda opción fluya al diálogo 11
c2.next_dialogue = d11
c2.save()

print("Nivel 1 insertado/actualizado correctamente.")


#nivel 2
# --- Nivel 2: Día 2 ---
# --- Crear personajes (si no existen todavía) ---
kove = Character.objects.get(name="Kove")
# Podemos asumir que otros personajes del día 2 son desconocidos (NPC)
desconocido = Character.objects.create(
    name="Desconocido",
    backstory="Compañero del patio, un poco tímido pero amigable",
    trait="Sociable, deportista",
    interesting="Le gusta el fútbol",
    personality="Amigable y extrovertido",
    is_friend=20
)

# --- Crear situación Día 2 ---
situacion_day2 = Situations.objects.create(
    title="Patio central: primer partido",
    day=2,
    locations=None,  # si ya tienes Location, asigna
    contexto_situation="Kove llega al patio y casi le golpea un balón",
    is_gameplay=True,
    orden_dialogue=0
)

# --- Crear diálogos ---
d1 = Dialogue.objects.create(
    situation=situacion_day2,
    character=kove,
    text="Es un patio muy amplio, veré que están jugando.",
    decision_point=False,
    lines_type="came_thought",
    orden=1
)

d2 = Dialogue.objects.create(
    situation=situacion_day2,
    character=desconocido,
    text="Disculpame, no fue mi intención asustarte, soy (nombre), ¿Quieres jugar un partido?, ya tenemos a un grupo.",
    decision_point=True,  # Punto de decisión
    lines_type="npc_speech",
    orden=2
)

# --- Crear opciones de decisión ---
# Decisión 1: Buena (aceptar jugar)
d3 = Dialogue.objects.create(
    situation=situacion_day2,
    character=desconocido,
    text="Dale!, lo pasarás bien, contigo tenemos los equipos armados para jugar",
    decision_point=False,
    lines_type="npc_speech",
    orden=3
)

d4 = Dialogue.objects.create(
    situation=situacion_day2,
    character=kove,
    text="Ok compañeros, yo he sido cadete de fútbol, así que daré lo mejor que pueda, marcaré muchos goles.",
    decision_point=False,
    lines_type="came_speech",
    orden=4
)

d5 = Dialogue.objects.create(
    situation=situacion_day2,
    character=kove,
    text="Ahora a disfrutar",
    decision_point=False,
    lines_type="came_thought",
    orden=5
)

c1 = Choice.objects.create(
    dialogue=d2,
    text_choice="Está bien, quiero divertirme un rato",
    consequence="Kove se une al partido y disfruta jugando con los compañeros.",
    next_dialogue=d3,
    order=1,
    type_choice="buena",
    friendship_points=10
)

# Decisión 2: Mala (no jugar)
d6 = Dialogue.objects.create(
    situation=situacion_day2,
    character=kove,
    text="Te doy las gracias, pero me siento un poco ansioso y prefiero estar observando.",
    decision_point=False,
    lines_type="came_speech",
    orden=6
)

d7 = Dialogue.objects.create(
    situation=situacion_day2,
    character=desconocido,
    text="No hay problema, tal vez en otra ocasión",
    decision_point=False,
    lines_type="npc_speech",
    orden=7
)

c2 = Choice.objects.create(
    dialogue=d2,
    text_choice="No, prefiero observar el partido",
    consequence="Kove se queda viendo el partido desde la distancia, la relación no avanza.",
    next_dialogue=d6,
    order=2,
    type_choice="neutral",  # 0 puntos de amistad
    friendship_points=0
)
#nivel 3
# --- Nivel 3: Día 3 ---
# --- Personajes del día 3 ---
kove = Character.objects.get(name="Kove")

desconocida = Character.objects.create(
    name="Desconocida",
    backstory="Chica popular pero amable, le gusta pintar",
    trait="Mandona, creativa",
    interesting="Le encanta pintar y dibujar",
    personality="Simpática y reflexiva",
    is_friend=20
)

# --- Crear situación Día 3 ---
situacion_day3 = Situations.objects.create(
    title="Cafetería exterior: nueva amiga",
    day=3,
    locations=None,  # asignar Location si lo tienes
    contexto_situation="Kove intenta presentarse a una chica popular y solitaria",
    is_gameplay=True,
    orden_dialogue=0
)

# --- Diálogos ---
d1 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="Parece que todas las mesas están ocupadas, bueno buscaré el sitio más alejado posible",
    decision_point=False,
    lines_type="came_thought",
    orden=1
)

d2 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="Bueno voy a empezar con un 'Hola'",
    decision_point=False,
    lines_type="came_thought",
    orden=2
)

d3 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="Hola... Me llamo Kove, un gusto",
    decision_point=False,
    lines_type="came_speech",
    orden=3
)

d4 = Dialogue.objects.create(
    situation=situacion_day3,
    character=desconocida,
    text="Mucho gusto, mi nombre es (name) *risas* porque te sentaste por acá",
    decision_point=False,
    lines_type="npc_speech",
    orden=4
)

d5 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="Parece ser que no había espacio por el lugar, lo siento si te incomodé",
    decision_point=False,
    lines_type="came_speech",
    orden=5
)

d6 = Dialogue.objects.create(
    situation=situacion_day3,
    character=desconocida,
    text="No te preocupes, yo también quería escapar un poco del ruido en el centro",
    decision_point=True,  # Punto de decisión
    lines_type="npc_speech",
    orden=6
)

# --- Crear opciones de decisión Día 3 ---
# Decisión 1: Buena (interesarme por dibujar)
d7 = Dialogue.objects.create(
    situation=situacion_day3,
    character=desconocida,
    text="La verdad es que dibujar es mi pasión",
    decision_point=False,
    lines_type="npc_speech",
    orden=7
)

c1 = Choice.objects.create(
    dialogue=d6,
    text_choice="Te gusta dibujar mucho entonces...",
    consequence="Kove pasa el recreo hablando sobre obras de arte y acercándose a una nueva amiga.",
    next_dialogue=d7,
    order=1,
    type_choice="buena",
    friendship_points=10
)

# Decisión 2: Mala (desinteresarse)
d8 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="No me parece divertido dibujar",
    decision_point=False,
    lines_type="came_speech",
    orden=8
)

d9 = Dialogue.objects.create(
    situation=situacion_day3,
    character=desconocida,
    text="Ok, entiendo… te puedes ir entonces",
    decision_point=False,
    lines_type="npc_speech",
    orden=9
)

c2 = Choice.objects.create(
    dialogue=d6,
    text_choice="No me interesa, prefiero irme",
    consequence="Kove se despide, la relación no avanza.",
    next_dialogue=d8,
    order=2,
    type_choice="neutral",
    friendship_points=0
)

# Decisión 3: No presentarme
d10 = Dialogue.objects.create(
    situation=situacion_day3,
    character=kove,
    text="Mejor no parece muy ocupada y mala onda, creo que es mejor no hacer nada, me estoy poniendo muy ansioso y nervioso",
    decision_point=False,
    lines_type="came_thought",
    orden=10
)

d11 = Dialogue.objects.create(
    situation=situacion_day3,
    character=desconocida,
    text="Me pregunto por qué se quedó tanto rato mirando y se fue, qué raro",
    decision_point=False,
    lines_type="npc_speech",
    orden=11
)

c3 = Choice.objects.create(
    dialogue=d6,
    text_choice="No me presento",
    consequence="Kove se retira sin interactuar, la relación no avanza.",
    next_dialogue=d10,
    order=3,
    type_choice="neutral",
    friendship_points=0
)

# --- Nivel 3: Día 4 ---
# Personaje del día 4
persona = Character.objects.create(
    name="Alicie",
    backstory="Amante de la música, escucha y toca instrumentos",
    trait="Creativa, sociable",
    interesting="Le gusta compartir playlists y tocar batería",
    personality="Amable y alegre",
    is_friend=20
)

# Situación Día 4
situacion_day4 = Situations.objects.create(
    title="Plaza: nueva amistad musical",
    day=4,
    locations=None,
    contexto_situation="Kove escucha música y se acerca una persona interesada en compartir gustos musicales",
    is_gameplay=True,
    orden_dialogue=0
)

# Diálogos Día 4
d1 = Dialogue.objects.create(
    situation=situacion_day4,
    character=kove,
    text="Esta música está muy buena",
    decision_point=False,
    lines_type="came_thought",
    orden=1
)

d2 = Dialogue.objects.create(
    situation=situacion_day4,
    character=persona,
    text="Hola que tal, ¿Qué música escuchas?",
    decision_point=True,  # Punto de decisión
    lines_type="npc_speech",
    orden=2
)

# Decisión 1: Buena
d3 = Dialogue.objects.create(
    situation=situacion_day4,
    character=kove,
    text="Claro, no tengo problema. ¿Tocas instrumentos? Podríamos hacer un cover de una canción de algún grupo que nos guste.",
    decision_point=False,
    lines_type="came_speech",
    orden=3
)

d4 = Dialogue.objects.create(
    situation=situacion_day4,
    character=persona,
    text="Obvio, toco la batería, soy bueno en eso. Me parece estupendo",
    decision_point=False,
    lines_type="npc_speech",
    orden=4
)

c1 = Choice.objects.create(
    dialogue=d2,
    text_choice="Claro, compartamos música y toquemos juntos",
    consequence="Kove inicia amistad musical con Alicie y hablan sobre formar un grupo",
    next_dialogue=d3,
    order=1,
    type_choice="buena",
    friendship_points=10
)

# Decisión 2: Mala
d5 = Dialogue.objects.create(
    situation=situacion_day4,
    character=kove,
    text="Mmm, no lo sé, en general no comparto mis playlists, las hago solamente para mí",
    decision_point=False,
    lines_type="came_speech",
    orden=5
)

d6 = Dialogue.objects.create(
    situation=situacion_day4,
    character=persona,
    text="Ok, está bien, lo entiendo. No hay problema",
    decision_point=False,
    lines_type="npc_speech",
    orden=6
)

c2 = Choice.objects.create(
    dialogue=d2,
    text_choice="Prefiero no compartir mis playlists",
    consequence="Kove mantiene distancia y la relación no avanza",
    next_dialogue=d5,
    order=2,
    type_choice="neutral",
    friendship_points=0
)

