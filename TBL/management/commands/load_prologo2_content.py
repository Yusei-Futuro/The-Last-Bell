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
            name="Álex",
            defaults={
                "backstory": "Un compañero del nuevo colegio, amistoso y curioso.",
                "interesting": "Siempre está dispuesto a hablar con los nuevos.",
                "personality": "Extrovertido y optimista."
            }
        )

    def create_locations(self):

        Location.objects.get_or_create(
            locations="Colegio",
            defaults={
                "descriptions": "Un gran edificio en la ciudad, donde Kove comenzará una nueva etapa escolar.",
                "imagen_fondo": "game_locations/Salon.png"
            }
        )

    def create_situation(self):
        # Primera parte del prólogo
        location_casa = Location.objects.get(locations="Casa de Came")
        location_colegio = Location.objects.get(locations="Colegio")
        kove = Character.objects.get(name="Came")

        situation2 = Situations.objects.create(
            day=0,
            title="El comienzo - Parte 2",
            locations=location_colegio,
            character=kove,
            contexto_situation="Segunda parte del primer día de clases"
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='narration',
            text="Después de un largo acto de apertura, Came entra a su nuevo salón de clases. Apenas escuchó lo importante, pero entendió que es un nuevo comienzo.",
            order=1,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_thought',
            character=Character.objects.get(name="Came"),
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
            character=Character.objects.get(name="Came"),
            text="Sí, me llamo Came. ¿Cómo te llamas?",
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
            character=Character.objects.get(name="Came"),
            text="Gracias, mucho gusto.",
            order=6,
            decision_point=False
        )

        Dialogue.objects.create(
            situation=situation2,
            line_type='came_thought',
            character=Character.objects.get(name="Came"),
            text="Vale... un poco más y entro. Respira... respira...",
            order=7,
            decision_point=False
        )