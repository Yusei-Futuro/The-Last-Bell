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
                "image_url": "game_characters/protagonista.png"
            }
        )

        Character.objects.get_or_create(
            name="Isabela",
            defaults={
                "backstory": "Le gusta estudiar y ayudar a sus compañeros",
                "interesting": "Filosofía y matemáticas",
                "personality": "Inteligente, algo curiosa",
                "is_friend": 20,
                "image_url": "game_characters/npc-4.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Sala de estudio",
            defaults={
                "descriptions": "Una sala tranquila con mesas y libros para estudiar",
                "imagen_fondo": "game_locations/saladeestudios.jpg"
            }
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Isabela")
        sala = Location.objects.get(locations="Sala de estudio")

        situation = Situations.objects.create(
            day=7,
            title="Estudio sorpresa",
            locations=sala,
            character=npc,
            contexto_situation="Came va a estudiar y conoce a Isabela, una compañera que lo ayudará.",
            moraleja="En el día siete se aplica tanto el manejo de la ira como la superación de la zona de confort al tener que socializar cuando uno está en una situación complicada pero si uno consigue sobrellevar el estrés, y logra aun así poder salir de su zona de confort al hablar y hacer algo que no estas acostumbrado hacer, como estudiar con alguien más, no solo se puede hacer un amigo sino que se puede superar el estrés y el problema más fácil",
            audio="sounds/salaestudioar.mp3"
        )


        line1 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Ahhhh, no he logrado estudiar para la prueba que tengo dentro del siguiente turno...", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, line_type='narration', text="Came corre a la sala de estudio de la escuela, agarra el primer libro que ve y se sienta al lado de alguien sin querer.", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, line_type='narration', text="Una chica lo mira confundida a través de unos lentes circulares.", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Creo que la he visto, en algún lugar.", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Creo que en mi clase, será que también vino a estudiar como yo.", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Hola, mucho gusto. ¿Vas a mi clase? Encantado de conocerte, ¿te parece bien si me ayudas un rato a estudiar?", order=6, decision_point=False)
        line7 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_thought', text="*Lo mira impactante* ... logra ver el libro ... *risitas*", order=7, decision_point=False)
        line8 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Me muero de vergüenza, debo presentarme.", order=8, decision_point=False)
        line9 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Mucho gusto, soy Came.", order=9, decision_point=False)
        line10 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="No es eso, sino que parece que vas a estudiar 'Filosofía' en vez de Matemáticas.", order=10, decision_point=False)
        line11 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="*No puede ser* Ahhh.", order=11, decision_point=False)
        line12 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="No te preocupes, solo cambia el libro. A propósito, mi nombre es Isabela, mucho gusto.", order=12, decision_point=False)
        line13 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="¿Te gustaría estudiar conmigo luego de que estudies 'Filosofía'?", order=13, decision_point=False)

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Que puedo decir?",
            order=14,
            decision_point=True
        )

#Ruta "Buena"

        line15 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Me parece bien. *Ríe*",
            order=15,
            decision_point=False
        )

        line16 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Pero yo no iba a estudiar eso jajaja.",
            order=16,
            decision_point=False
        )

        line17 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Sí, claro. Nunca había visto a alguien tan apurado por comprender la 'Filosofía'.",
            order=17,
            decision_point=False
        )

        line18 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Me confundí de libro, okey.",
            order=18,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came y Isabela pasaron estudiando juntos antes de la prueba. Aunque le fue mal, le encantó conocer a una compañera de estudio.",
            order=19,
            decision_point=False
        )
        
#Ruta """Mala""""" - Gap para separar rutas
        line20 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="*Came le voltea con indignación*",
            order=30,
            decision_point=False
        )

        line21 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came se retira con el libro, Isabela queda confundida pero regresa porque sabía que podría ayudarlo.",
            order=31,
            decision_point=False
        )

        line22 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Volviste… pensaba que no.",
            order=32,
            decision_point=False
        )

        line23 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Ojalá ser filósofo para intentar comprender porque el profesor parece que nos odia con dicha prueba.",
            order=33,
            decision_point=False
        )

        line24 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="A que es cierto, creo que es abusador con nosotros y nos odia porque le fue mal en la universidad con matemáticas.",
            order=34,
            decision_point=False
        )

        line25 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="*Risas* Bueno a estudiar.",
            order=35,
            decision_point=False
        )

        line26 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Pasaron horas conversando sobre cómo el profesor enseña cálculo integral a niños de 16 años, Came se lamenta por ellos.",
            order=36,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Me parece bien.",
            consequence="Came y Isabela pasan estudiando juntos antes de la prueba.",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line15
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="No quiero estudiar con ella.",
            consequence="Came se retira con el libro, pero Isabela regresa porque quería ayudarlo.",
            friendship_points=-10,
            type_choice='mala',
            order=2,
            next_dialogue=line20
        )