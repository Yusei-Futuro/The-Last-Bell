#Nivel que falta codificar
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
            name="Lisa",
            defaults={
                "backstory": "Parece ser popular pero amable",
                "interesting": "Le gusta pintar y dibujar",
                "personality": "Mandona pero buena gente",
                "is_friend": 20,
                "image_url": "game_characters/npc-3.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Cafetería exterior",
            defaults={
                "descriptions": "Una cafetería con mesas al aire libre, ambiente concurrido pero relajado",
                "imagen_fondo": "game_locations/Cafeteria.jpg"
            }
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Lisa")
        cafeteria = Location.objects.get(locations="Cafetería exterior")

        situation = Situations.objects.create(
            day=3,
            title="Conociendo a alguien nuevo",
            locations=cafeteria,
            character=npc,
            contexto_situation="Parece que para ser bastante popular está solita, podríamos intentar acompañarla. Creo que no me haría mal tener una amiga.",
            moraleja="En el día tres también es una muestra de la importancia de la empatía en las relaciones sociales ya que debemos entender los gustos de cada persona y no solo quedarnos con lo que creemos nosotros, si somos considerados podemos formar una conversación de agrado mutuo y aprender de otras personas cosas nuevas que a la larga nos pueden servir, además de fortalecer la relación que se tiene con esa persona"
        )

        line1 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Parece que todas las mesas están ocupadas, bueno buscaré el sitio más alejado posible.", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, line_type='narration', text="Came se sienta al fondo de la cafeteria.", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, character=came, line_type='narration', text="En la mesa de alado hay una chica que parece ser que esta dibujando", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=came, line_type='narration', text="Se escucha un ruido en su mesa de repente", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=came, line_type='npc_speech', text="AAAAAA mi dibujo se arrunio", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=npc, line_type='narration', text="Came se levanta rapidamente con servilletas para ayudarla", order=6, decision_point=False)
        line7 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Toma aqui tienes una servilleta", order=7, decision_point=False)
        line8 = Dialogue.objects.create(situation=situation, line_type='narration', text="La chica lo agarra y se pone a limpiar el desorden", order=8, decision_point=False)
        line9 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Muchas gracias por la ayuda, me presento, mi nombre es Lisa y tu eres?", order=9, decision_point=False)
        line10 = Dialogue.objects.create(situation=situation, character=npc, line_type='came_speech', text="Mi nombre es Came mucho gusto", order=10, decision_point=False)
        line11 = Dialogue.objects.create(situation=situation, character=came, line_type='narration', text="Came mira el desorden mientras Lisa intenta salvar su dibujo", order=11, decision_point=False)
        line12 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Esta arruinado", order=12, decision_point=False)
        line13 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="No realmente", order=13, decision_point=False)
        line14 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Realmente lo crees", order=14, decision_point=False)
        line15 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="No del todo, creo que puede ser otra forma de arte, si pintas sobre el cafe", order=15, decision_point=False)
        line16 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="JAJAJA no creo, me parece imposible pensar que puedo pintar sobre cafe", order=16, decision_point=False)
        
        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='narration',
            text="Came mira el dibujo y tiene una idea",
            order=17,
            decision_point=True
        )

# Ruta mala
        line21 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Me permites",
            order=18,
            decision_point=False
        )

        line22 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Claro aqui tienes",
            order=19,
            decision_point=False
        )

        line23 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='narration',
            text="Came le tira mas cafe sobre el dibujo",
            order=20,
            decision_point=False
        )

        line24 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Que haces, estas loco, no te pedi que le hicieras eso a mi dibujo, esta oficialmente arruinado.",
            order=21,
            decision_point=False
        )

        line25 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Porque se enojara tanto, no entiendo si quedaria mejor",
            order=22,
            decision_point=False
        )

        line26 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Lisa se calma y le pide si se puede ir",
            order=23,
            decision_point=False
        )

# Ruta buena - Gap para separar rutas
        line18 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="... Para que quede un delineado mejor",
            order=30,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="No entiendo muy bien a què te refieres",
            order=31,
            decision_point=False
        )

        line20 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came agarro el làpiz, mientras le explicaba la tecnica de la que hablaba, mientras Lisa asentia y asi pasaron 3 horas juntos.",
            order=32,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Decirle que puedes remarcar las lineas",
            consequence="Oye, creo que puedes remarcar las lineas",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line18
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Pedir el vaso con cafe para hacer arte",
            consequence="Me prestas el vaso con cafe",
            friendship_points=-20,
            type_choice='mala',
            order=2,
            next_dialogue=line21
        )