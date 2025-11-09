from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice


class Command(BaseCommand):
    help = 'Carga el contenido del Prólogo'

    def handle(self, *args, **kwargs):
        self.create_characters()
        self.create_locations()
        self.create_situation()
        self.stdout.write(self.style.SUCCESS('Contenido del Prólogo cargado exitosamente!'))

    def create_characters(self):
        Character.objects.get_or_create(
            name="Came",
            defaults={
                "backstory": "Un chico que acaba de mudarse a una nueva ciudad junto a su madre.",
                "interesting": "Le gusta jugar videojuegos hasta tarde.",
                "personality": "Tranquilo, distraído, pero amable.",
                "image_url": "game_characters/protagonista.png"
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

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Casa de Came",
            defaults={
                "descriptions": "El nuevo hogar de Kove y su madre, aún lleno de cajas sin desempacar.",
                "imagen_fondo": "game_locations/Habitacion.png"
            }
        )

    def create_situation(self):
        # Primera parte del prólogo
        location_casa = Location.objects.get(locations="Casa de Came")
        kove = Character.objects.get(name="Came")

        situation1 = Situations.objects.create(
            day=-1,
            title="El comienzo - Parte 1",
            locations=location_casa,
            character=kove,
            contexto_situation="Primera parte del primer día de clases"
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
            character=Character.objects.get(name="Came"),
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
            character=Character.objects.get(name="Came"),
            text="¡Sí mamá!",
            order=6,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation1,
            line_type='narration',
            text="Came baja corriendo las escaleras y sale apurado por la puerta, casi atragantándose con la comida.",
            order=7,
            decision_point=False
        )