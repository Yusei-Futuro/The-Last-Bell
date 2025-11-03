from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice

class Command(BaseCommand):
    help = 'Carga el contenido del Día 1 desde dialogos.txt'

    def handle(self, *args, **kwargs):
        self.create_characters()
        self.create_locations()
        self.create_situation()
        self.stdout.write(self.style.SUCCESS('Contenido del Día 1 cargado exitosamente!'))

    def create_characters(self):
        Character.objects.get_or_create(
            name="Came",
            defaults={
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "interesting": "Leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20,
                "image_url": "game_characters/player.png"
            }
        )

        Character.objects.get_or_create(
            name="Sandro",
            defaults={
                "backstory": "Le encanta el ajedrez y compartir tácticas con otros",
                "interesting": "Jugar ajedrez y estudiar partidas famosas",
                "personality": "Amigable y paciente",
                "is_friend": 20,
                "image_url": "game_characters/npc-5.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Banca exterior",
            defaults={
                "descriptions": "Una banca en el patio, rodeada de árboles y otras personas estudiando."
            }
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Sandro")
        banca = Location.objects.get(locations="Banca exterior")

        situation = Situations.objects.create(
            day=5,
            title="Una partida inesperada de ajedrez",
            locations=banca,
            character=came,
            contexto_situation="Came está leyendo un libro de ajedrez en una banca cuando un desconocido se le acerca para interactuar."
        )

# Diálogos introductorios
        line1 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Está bueno este libro de ajedrez, aprenderé todos los ataques y defensas posibles.", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Últimamente me parece agradable el ajedrez", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, line_type='narration', text="Llega un desconocido.", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Hola, a mí también me gusta el ajedrez. ¿Hablamos de algunas tácticas?", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Ese libro que estás leyendo es muy bueno, a mí también me gustan los libros de ajedrez y las partidas de Bobby Fisher", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Mucho gusto, me llamo Sandro", order=6, decision_point=False)
        line7 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Quién es esta persona, parece bastante amigable. Creo que igual que yo está interesado.", order=7, decision_point=False)
        line8 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Hola, soy Came", order=8, decision_point=False)
        line9 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Estoy aprendiendo el Gambito de Rey", order=9, decision_point=False)
        line10 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Ese ataque es muy poderoso pero...", order=10, decision_point=False)
        line11 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Tiene demasiadas aperturas porque deja al Rey muy expuesto, pero si se juega bien te dejará en una posición ganadora al inicio", order=11, decision_point=False)
        line12 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="...", order=12, decision_point=False)
        line13 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Creo que me pasé", order=13, decision_point=False)
        line14 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Eso es fascinante, es mi favorita. Te gustaría jugar algunas partidas pero no tenemos un tablero aquí...", order=14, decision_point=False)

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="¿Qué harás, Came?",
            order=15,
            decision_point=True
        )

#Ruta Buena

        line16 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Yo tengo un tablero.",
            order=16,
            decision_point=False
        )

        line17 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came agarra el tablero y lo pone sobre la mesa.",
            order=17,
            decision_point=False
        )

        line18 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Sandro se empieza a reír.",
            order=18,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Pasaron el recreo jugando. Sandro no le dejó ganar ni una vez, olvidando mencionar que era Gran Master.",
            order=19,
            decision_point=False
        )

#Ruta Mala - Gap para separar rutas

        line20 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="No tengo tablero en este lugar, lo siento mucho.",
            order=30,
            decision_point=False
        )

        line21 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Don't worry, otro día jugamos. ¿Te gustaría seguir hablando de tácticas un poco?",
            order=31,
            decision_point=False
        )

        line22 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Pasaron los minutos hablando sobre partidas viejas hasta que Came se aburrió y se fue.",
            order=32,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Interrumpir y usar tu propio tablero",
            consequence="Yo tengo un tablero.",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line16
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Decir que no tienes tablero",
            consequence="No tengo tablero en este lugar, lo siento mucho.",
            friendship_points=-10,
            type_choice='mala',
            order=2,
            next_dialogue=line20
        )