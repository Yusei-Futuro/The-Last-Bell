from tkinter import image_names

from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice


class Command(BaseCommand):
    help = 'Carga el contenido del Día 1 desde dialogos.txt'

    def create_characters(self):
        Character.objects.get_or_create(
            name="Kove",
            defaults={
                "backstory": "Un chico que acaba de mudarse a una nueva ciudad junto a su madre.",
                "interesting": "Le gusta jugar videojuegos hasta tarde.",
                "personality": "Tranquilo, distraído, pero amable."
            }
        )

        Character.objects.get_or_create(
            name="Madre",
            defaults={
                "backstory": "La madre de Kove, cariñosa pero estricta con los horarios.",
                "interesting": "Siempre prepara desayuno aunque Kove se despierte tarde.",
                "personality": "Paciente pero práctica."
            }
        )

        Character.objects.get_or_create(
            name="Álex",
            defaults={
                "backstory": "Un compañero del nuevo colegio, amistoso y curioso.",
                "interesting": "Siempre está dispuesto a hablar con los nuevos.",
                "personality": "Extrovertido y optimista."
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            name="Casa de Kove",
            defaults={
                "description": "El nuevo hogar de Kove y su madre, aún lleno de cajas sin desempacar."
            }
        )

        Location.objects.get_or_create(
            name="Colegio",
            defaults={
                "description": "Un gran edificio en la ciudad, donde Kove comenzará una nueva etapa escolar."
            }
        )
    def create_situation(self):
# Primera parte del prólogo
        location_casa = Location.objects.get(name="Casa de Kove")
        location_colegio = Location.objects.get(name="Colegio")

        situation1 = Situations.objects.create(
            title="El comienzo de una nueva vida",
            act="Acto 1: Day 1",
            context="Primera parte del primer día de clases",
            location=location_casa
        )

# Diálogos
        Dialogue.objects.create(
            situation=situation1,
            line_type='narration',
            text="Despertamos como en un día cualquiera en nuestra nueva casa. Hace poco nos mudamos por el nuevo trabajo de mi mamá.",
            order=1,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='narration',
            text="Estamos medios cansados por jugar videojuegos hasta muy tarde, pero el problema principal es que parece que llego tarde a mi primer día de escuela.",
            order=2,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='npc_speech',
            character=Character.objects.get(name="Madre"),
            text="¡Hijo! Vamos tarde a tu primer día de escuela, termina de comer rápido.",
            order=3,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='came_speech',
            character=Character.objects.get(name="Kove"),
            text="¡Perdón mamá! Termino de comer altiro.",
            order=4,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='npc_speech',
            character=Character.objects.get(name="Madre"),
            text="¡No olvides tu mochila!",
            order=5,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='came_speech',
            character=Character.objects.get(name="Kove"),
            text="¡Sí mamá!",
            order=6,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='narration',
            text="Kove baja corriendo las escaleras y sale apurado por la puerta, casi atragantándose con la comida.",
            order=7,
            decision_point=False
        )
         
# Segunda parte del prólogo
        situation2 = Situations.objects.create(
            title="El comienzo de una nueva vida - Parte 2",
            act="Acto 1: Day 1",
            context="Segunda parte del primer día de clases",
            location=location_colegio
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='narration',
            text="Después de un largo acto de apertura, Kove entra a su nuevo salón de clases. Apenas escuchó lo importante, pero entendió que es un nuevo comienzo.",
            order=1,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_thought',
            character=Character.objects.get(name="Kove"),
            text="Ok, solo entro y saludo. Nadie tiene que saber que soy diferente.",
            order=2,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='npc_speech',
            character=Character.objects.get(name="Álex"),
            text="Hola, ¿tú también eres nuevo?",
            order=3,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_speech',
            character=Character.objects.get(name="Kove"),
            text="Sí, me llamo Kove. ¿Cómo te llamas?",
            order=4,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='npc_speech',
            character=Character.objects.get(name="Álex"),
            text="Me llamo Álex, mucho gusto.",
            order=5,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_speech',
            character=Character.objects.get(name="Kove"),
            text="Gracias, mucho gusto.",
            order=6,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_thought',
            character=Character.objects.get(name="Kove"),
            text="Vale... un poco más y entro. Respira... respira...",
            order=7,
            decision_point=False
        )