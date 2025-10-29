from tkinter import image_names

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
            name="Kove",
            defaults={
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "interesting": "Leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20
            }
        )

        Character.objects.get_or_create(
            name="Bibliotecario Zu",
            defaults={
                "backstory": "Ama los libros y disfruta compartir su conocimiento",
                "interesting": "Leer y recomendar libros",
                "personality": "Paciente y observador",
                "is_friend": 20
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Biblioteca Central",
            defaults={
                "descriptions":"Una biblioteca grande y fuerte con muros y libros nada intimidantes para came"},
        )

    def create_situation(self):
        bibliotecario = Character.objects.get(name="Bibliotecario Zu")
        biblioteca = Location.objects.get(locations="Biblioteca Central")

        situation = Situations.objects.create(
            day=1,
            title="Conflicto por el libro",
            locations=biblioteca,
            character=bibliotecario,
            contexto_situation="Came busca un libro de fantasía pero alguien más lo quiere también."
        )

        line1=Dialogue.objects.create(situation=situation, line_type='narration', text="Mmmm parece ser la biblioteca central de la escuela...", order=1,decision_point=False)
        line2=Dialogue.objects.create(situation=situation, line_type='came_thought', text="Me pregunto si tendrán la nueva edición de Las aventuras por monje chino por Japon", order=2,decision_point=False)
        line3=Dialogue.objects.create(situation=situation, line_type='came_thought', text="Me encantaría leer la nueva aventura de Sandra Martínez.", order=3,decision_point=False)
        line4=Dialogue.objects.create(situation=situation, line_type='narration', text="Luego de un rato logra encontrar el libro, pero alguien más lo toma a la vez.", order=4,decision_point=False)
        line5=Dialogue.objects.create(situation=situation, line_type='narration', text="Sus manos chocan sobre la portada del libro.", order=5,decision_point=False)

        line6=Dialogue.objects.create(
            situation=situation,
            line_type="npc_speech",
            text="¿Quien eres y porque tocas mi libro?",
            order=6,
            decision_point=False
        )
        line7=Dialogue.objects.create(
            situation=situation,
            line_type='came_speech',
            text="Tu libro, yo lo vi primero es mío este libro ",
            order=7,
            decision_point=False
        )
        line8=Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came toma el libro y intenta huir pero lo toman de la espalda",
            order=8,
            decision_point=False
        )

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=bibliotecario,
            line_type='npc_speech',
            text="Disculpa mis modales, me llamo Zu y me gusta leer. Llevo mucho tiempo buscando salió hace poco y me emocione un poco al verlo ¿crees poder disculparme?",
            order=9,
            decision_point=True
        )

        Choice.objects.create(
            dialogue=decision_line,
            text_choice="Aceptar las disculpas de Zu",
            consequence="Sí, lo siento también es mi culpa por actuar así...",
            friendship_points=20,
            type_choice='buena',
            order=1,

        )
#Falta la parte de next dialogue
        Choice.objects.create(
            dialogue=decision_line,
            text_choice="Ignorar las disculpas de Zu",
            consequence="No las acepto, pareces una mala persona.",
            friendship_points=-20,
            type_choice='mala',
            order=2,

        )

        #Ruta mala
        line10=Dialogue.objects.create(
            situation=situation,
            line_type='came_thought',
            text="Me estoy enojando bastante",
            order=10,
            decision_point=False
        )
        line11=Dialogue.objects.create(
            situation=situation,
            line_type='came_speech',
            text=" No las acepto, no puedes quitarme mi libro, es mio porque yo lo vi",
            order=11,
            decision_point=False
        )
        line12=Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came se gira rapido y huye de la escena",
            order=12,
            decision_point=False
        )

        line13=Dialogue.objects.create(
            situation=situation,
            line_type='npc_speech',
            text="Parece que tu no eres capaz de pensar en los demás, piensas acaso que eres unico en el mundo ",
            order=13,
            decision_point=False
        )

        #Ruta buena
        line14=Dialogue.objects.create(
            situation=situation,
            line_type='came_thought',
            text=" Será que este puede ser amigo mío… Respira… me he comportado de mala manera parece, lo arreglare",
            order=14,
            decision_point=False
        )
        line15=Dialogue.objects.create(
            situation=situation,
            line_type='came_speech',
            text="Sí lo siento tambien es mi culpa por actuar así, me comporte también mal lo lamento, mi nombre es Came un placer Zu",
            order=15,
            decision_point=False
        )
        line16=Dialogue.objects.create(
            situation=situation,
            line_type='npc_speech',
            text="Ok Came, pareces ser alguien que le gusta mucho leer por lo que parece, lees mucho sobre este autor",
            order=16,
            decision_point=False
        )
        line17=Dialogue.objects.create(
            situation=situation,
            line_type='came_speech',
            text="Siii me encanta, lo leo todos los días, mi historia favorita es Las aventuras por monje chino por Japon porque me encanta cuando pelea con la bestia al final de la trilogía de fiction, es fascinante su manera de escribir que logra recrear en mi mente toda la batalla plis plas plus.",
            order=17,
            decision_point=False
        )
        line18=Dialogue.objects.create(
            situation=situation,
            line_type='npc_thought',
            text="Estoy seguro de que me acaban de hacer un gran spoiler",
            order=18,
            decision_point=False
        )
        line19=Dialogue.objects.create(
            situation=situation,
            line_type='npc_thought',
            text="Voy a pedirle haber si podemos leer juntos el libro",
            order=19,
            decision_point=False
        )
        line20=Dialogue.objects.create(
            situation=situation,
            line_type='npc_speech',
            text="Te parece si podemos ...",
            order=20,
            decision_point=False
        )
        line21=Dialogue.objects.create(
            situation=situation,
            line_type='came_speech',
            text="Y te gusta el segundo libro de la trilogía, es fascinante porque trata de esto y lo otro….",
            order=21,
            decision_point=False
        )
        line21=Dialogue.objects.create(
            situation=situation,
            line_type='npc_thought',
            text="Pues parece que no voy a poder detenerlo JAJAJA",
            order=21,
            decision_point=False
        )
        line22=Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Bueno durante todo el recreo estuvieron hablando sobre la famosa trilogía Las aventuras por monje chino por Japon bueno name hablo poco pero a Came le gusto sentirse escuchado por alguien que entiende sus gustos, se sintió muy bien",
            order=22,
            decision_point=False
        )