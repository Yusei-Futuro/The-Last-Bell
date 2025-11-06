from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice

class Command(BaseCommand):
    help = 'Carga el contenido del Dia 2 desde dialogos.txt'

    def handle(self, *args, **kwargs):
        self.create_characters()
        self.create_locations()
        self.create_situation()
        self.stdout.write(self.style.SUCCESS("Dia 2 del juego cargado correctamente"))

    def create_characters(self):
        Character.objects.get_or_create(
            name="Came",
            defaults={ 
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "interesting": "Leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20,
                "image_url": "game_characters/protagonista.png"
            }
        )

        Character.objects.get_or_create(
            name="Brad",
            defaults={
                "backstory": "Le encanta el futbol y socializar con nuevos compañeros",
                "interesting": "Jugar y enseñar futbol",
                "personality": "Amistoso y motivador",
                "is_friend": 20,
                "image_url": "game_characters/Brad.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Patio",
            defaults={
                "descriptions":"Un Amplio Patio con na cancha de futbol y espacio para el recreo",
                "imagen_fondo": "game_locations/Cancha de futbol.jpg"}

        )
        

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name = "Brad")
        patio = Location.objects.get(locations= "Patio")

        situation = Situations.objects.create(
            day=2,
            title="Una invitacion inesperada",
            locations=patio,
            character=npc,
            contexto_situation="Came es invitado a jugar un partido de futbol por un nuevo compañero"
        )
        
        line1 = Dialogue.objects.create(situation=situation, line_type='narration', text="Came llega al patio y observa el amplio espacio.", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Es un patio muy amplio, veré qué están jugando.", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, line_type='narration', text="De repente, un balón viene hacia él y logra esquivarlo.", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="¡Wow! eso estuvo cerca, ¿Quién tiró ese balón?", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Disculpame, no fue mi intención asustarte, soy Brad. ¿Quieres jugar un partido? Ya tenemos un grupo.", order=5, decision_point=False)

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Decido si jugar o no con ellos",
            order=6,
            decision_point=True
        )


# Ruta mala
        line7 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Me siento un poco nervioso con tanta gente.",
            order=7,
            decision_point=False

        )

        line8 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Gracias, pero prefiero observar por ahora.",
            order=8,
            decision_point=False
        )

        line9 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came se aleja y observa el partido desde lejos.",
            order=9,
            decision_point=False
        )

        line10 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="No hay problema, tal vez en otra ocasión.",
            order=10,
            decision_point=False
        )

# Ruta buena - Gap de orders para separar rutas
        line11 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="¡Genial! Me animaré a jugar y divertirme.",
            order=20,
            decision_point=False
        )

        line12 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="¡Está bien, acepto jugar! Me llamo Came, un gusto.",
            order=21,
            decision_point=False
        )

        line13 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="¡Perfecto Came! vamos a organizar los equipos.",
            order=22,
            decision_point=False
        )

        line14 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Me encanta el fútbol, daré lo mejor de mí en este partido.",
            order=23,
            decision_point=False
        )

        line15 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="Parece que es bueno jugando, espero que no me gane en goles JAJA",
            order=24,
            decision_point=False
        )

        line16 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Todos se organizan en equipos y el partido comienza con entusiasmo.",
            order=25,
            decision_point=False
        )

        line17 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Qué divertido es esto, me alegro de haber decidido jugar.",
            order=26,
            decision_point=False
        )

        line18 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="¡Buen trabajo Came, eres un gran compañero!",
            order=27,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Durante el partido, Came y Compa cooperan y marcan algunos goles.",
            order=28,
            decision_point=False
        )

        line20 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Me siento más integrado con mis compañeros, esto fue una buena decisión.",
            order=29,
            decision_point=False
        )

        line21 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="El recreo termina y todos regresan al aula, pero Came se siente contento y motivado para el próximo partido.",
            order=30,
            decision_point=False
        )

        # Crear choices y asignar next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Aceptar jugar",
            consequence="Está bien, quiero divertirme un rato",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line11
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="No jugar, solo observar",
            consequence="Prefiero mirar un poco y decidir después",
            friendship_points=0,
            type_choice='mala',
            order=2,
            next_dialogue=line7
        )


