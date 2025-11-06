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
            name="Bibliotecario Zu",
            defaults={
                "backstory": "Ama los libros y disfruta compartir su conocimiento",
                "interesting": "Leer y recomendar libros",
                "personality": "Paciente y observador",
                "is_friend": 20,
                "image_url": "game_characters/npc-1.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Biblioteca Central",
            defaults={
                "descriptions": "Una biblioteca grande y fuerte con muros y libros nada intimidantes para Came",
                "imagen_fondo": "game_locations/Libreria_escolar.jpg"
            },
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Bibliotecario Zu")
        biblioteca = Location.objects.get(locations="Biblioteca Central")

        situation = Situations.objects.create(
            day=1,
            title="Conflicto por el libro",
            locations=biblioteca,
            character=npc,
            contexto_situation="Came busca un libro de fantasía pero alguien más lo quiere también."
        )

        line1 = Dialogue.objects.create(situation=situation, line_type='narration', text="Mmmm parece ser la biblioteca central de la escuela...", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Me pregunto si tendrán la nueva edición de Las aventuras por monje chino por Japon", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Me encantaría leer la nueva aventura de Sandra Martínez.", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, line_type='narration', text="Luego de un rato logra encontrar el libro, pero alguien más lo toma a la vez.", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, line_type='narration', text="Sus manos chocan sobre la portada del libro.", order=5, decision_point=False)

        line6 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type="npc_speech",
            text="¿Quién eres y por qué tocas mi libro?",
            order=6,
            decision_point=False
        )
        line7 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="¿Tu libro? Yo lo vi primero, es mío este libro.",
            order=7,
            decision_point=False
        )
        line8 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came toma el libro e intenta huir, pero lo toman de la espalda.",
            order=8,
            decision_point=False
        )

        # Línea donde ocurre la decisión
        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Disculpa mis modales, me llamo Zu y me gusta leer. Llevo mucho tiempo buscando este libro, salió hace poco y me emocioné un poco al verlo. ¿Crees poder disculparme?",
            order=9,
            decision_point=True
        )

        # Crear las opciones (choices)
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Aceptar las disculpas de Zu",
            consequence="Sí, lo siento también es mi culpa por actuar así...",
            friendship_points=20,
            type_choice='buena',
            order=1,
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Ignorar las disculpas de Zu",
            consequence="No las acepto, pareces una mala persona.",
            friendship_points=-20,
            type_choice='mala',
            order=2,
        )

        # --- RUTA MALA ---
        line10 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Me estoy enojando bastante.",
            order=10,
            decision_point=False
        )
        line11 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="No las acepto, no puedes quitarme mi libro. Es mío porque yo lo vi.",
            order=11,
            decision_point=False
        )
        line12 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came se gira rápido y huye de la escena.",
            order=12,
            decision_point=False
        )
        line13 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Parece que no eres capaz de pensar en los demás. ¿Acaso crees que eres único en el mundo?",
            order=13,
            decision_point=False
        )

        # --- RUTA BUENA ---
        # NOTA: Los orders empiezan en 20 para crear un gap y evitar solapamiento con ruta mala
        line14 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="¿Será que este puede ser amigo mío? Respira… Me he comportado de mala manera, parece. Lo arreglaré.",
            order=20,
            decision_point=False
        )
        line15 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Sí, lo siento también es mi culpa por actuar así. Me comporté mal, lo lamento. Mi nombre es Came, un placer Zu.",
            order=21,
            decision_point=False
        )
        line16 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Ok Came, pareces alguien a quien le gusta mucho leer. ¿Lees mucho sobre este autor?",
            order=22,
            decision_point=False
        )
        line17 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="¡Sí! Me encanta, lo leo todos los días. Mi historia favorita es *Las aventuras por monje chino por Japón* porque me encanta cuando pelea con la bestia al final de la trilogía. Es fascinante su manera de escribir, logra recrear en mi mente toda la batalla.",
            order=23,
            decision_point=False
        )
        line18 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="Estoy seguro de que me acaban de hacer un gran spoiler.",
            order=24,
            decision_point=False
        )
        line19 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="Voy a pedirle a ver si podemos leer juntos el libro.",
            order=25,
            decision_point=False
        )
        line20 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="¿Te parece si lo leemos juntos alguna vez?",
            order=26,
            decision_point=False
        )
        line21 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="¿Y te gusta el segundo libro de la trilogía? Es fascinante porque trata de esto y lo otro…",
            order=27,
            decision_point=False
        )
        line22 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="Parece que no voy a poder detenerlo JAJAJA.",
            order=28,
            decision_point=False
        )
        line23 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Durante todo el recreo hablaron sobre la trilogía *Las aventuras por monje chino por Japón*. Zu habló poco, pero a Came le gustó sentirse escuchado por alguien que entendía sus gustos.",
            order=29,
            decision_point=False
        )

        # --- CONEXIÓN ENTRE CHOICES Y DIÁLOGOS ---
        choice_buena.next_dialogue = line14
        choice_mala.next_dialogue = line10

        choice_buena.save()
        choice_mala.save()
