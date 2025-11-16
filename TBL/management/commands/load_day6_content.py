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
            name="Aldo",
            defaults={
                "backstory": "Interesado en deportes y trabajo en equipo",
                "interesting": "Acrosport y deportes de grupo",
                "personality": "Sociable y motivador",
                "is_friend": 20,
                "image_url": "game_characters/Leonardo.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Gimnasio",
            defaults={
                "descriptions": "Gimnasio escolar con canchas y espacio para acrosport.",
                "imagen_fondo": "game_locations/gimnasio.jpg"}
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Aldo")
        gimnasio = Location.objects.get(locations="Gimnasio")


        situation = Situations.objects.create(
            day=6,
            title="Clase de Educación Física",
            locations=gimnasio,
            character=came,
            contexto_situation="En la clase de educación física el profesor les asigna dos opciones: armar acrosport o una clase de algún deporte. Came conocerá a una persona.",
            moraleja="En el día seis más que elegir si hacer una actividad en conjunto es la elección de cómo expresar el disgusto o lo incomodidad con la gente una habilidad muy necesaria si se quiere tener una buena convivencia con lo otros, el problema es cómo se comunica este disgusto, empáticamente, con amabilidad y respeto con el otro, o simplemente descartar cualquier modo de pensar ajeno y no intentar llegar a un consenso con otros"
        )

        line1 = Dialogue.objects.create(situation=situation, line_type='narration', text="Mmmm parece ser el gimnasio de la escuela...", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="No estoy seguro qué opción elegir, mejor escuchar primero a los demás.", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, line_type='narration', text="Luego de un momento, un compañero se acerca a Came para presentarse.", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Hola, me presento, mi nombre es Aldo... ¿Y tú? ¿Cómo te llamas?", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Mucho gusto, me llamo Came.", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Igualmente. ¿Has pensado en alguna opción que te guste?", order=6, decision_point=False)

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Aún no lo tengo claro. ¿Tienes alguna opción?",
            order=7,
            decision_point=True
        )

# Ruta mala (rechazar acrosport)

        line8 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Gracias por preguntar Aldo. Pero no quiero acrosport, prefiero deportes más comunes como fútbol o básquet.",
            order=8,
            decision_point=False
        )

        line9 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Si? Yo pensaba que el acrosport sería más entretenido y hasta más sencillo.",
            order=9,
            decision_point=False
        )

        line10 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Es probable, pero no quiero cargar a personas o hacer pirámides. Igual puedes buscar otra pareja.",
            order=10,
            decision_point=False
        )

        line11 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Ok.. Bueno, preguntaré a alguien más.",
            order=11,
            decision_point=False
        )

        line12 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Yo también buscaré a otra persona interesada en armar una clase, cuidate.",
            order=12,
            decision_point=False
        )

# Ruta buena (aceptar acrosport) - Gap para separar rutas
        line13 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Gracias por invitarme, Aldo. Me parece una buena elección, pero también podríamos hacer otra clase deportiva juntos.",
            order=20,
            decision_point=False
        )

        line14 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Entiendo. El acrosport me parece más entretenido y menos competitivo.",
            order=21,
            decision_point=False
        )

        line15 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Totalmente. Si organizamos la clase será divertido y no tiene que ser competitivo, podemos disfrutarlo juntos.",
            order=22,
            decision_point=False
        )

        line16 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Suena entretenido. ¿Tienes algún deporte en mente?",
            order=23,
            decision_point=False
        )
        line17 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Tal vez fútbol o básquet, me adapto a cualquiera. Lo importante es hacerlo juntos.",
            order=24,
            decision_point=False
        )

        line18 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Ok, me convenciste, vamos a armar la clase entonces.",
            order=25,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Aceptar la invitación de Aldo a hacer acrosport",
            consequence="Sí, gracias Aldo, me parece una buena elección.",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line13
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Rechazar acrosport y proponer otro deporte",
            consequence="Prefiero hacer alguna clase de algún deporte, tipo fútbol o básquet.",
            friendship_points=-10,
            type_choice='mala',
            order=2,
            next_dialogue=line8
        )