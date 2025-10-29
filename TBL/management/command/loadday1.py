from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice

class Command(BaseCommand):
    help = 'Carga el contenido del Día 1 desde dialogos.txt'

    def handle(self, *args, **kwargs):
        self.create_characters()
        self.create_locations()
        self.create_situations()
        self.create_dialogues()

        self.stdout.write(self.style.SUCCESS('Contenido del Día 1 cargado exitosamente!'))

    def create_characters(self):
        # Álex
        Character.objects.get_or_create(
            name="Álex",
            defaults={
                'backstory': 'Compañero nuevo que saluda antes de entrar a clase',
                'interests': 'Socializar',
                'personality': 'Amigable y abierto',
                'friendship_threshold': 20
            }
        )
        #Kove
        Character.objects.get_or_create(
            name="Kove",
            defaults={
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "trait": "Reservado, curioso",
                "interesting": "Le encanta leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20
            }
        )
        #Mama
        Character.objects.get_or_create(
            name="Mamá",
            defaults={
                "backstory": "Madre de Kove, trabaja mucho y se preocupa por su hijo",
                "trait": "Protector, estricto",
                "interesting": "Le gusta mantener todo organizado",
                "personality": "Cariñosa pero estricta",
                "is_friend": 0
            }
        )
        #Bibliotecario Zu
        Character.objects.get_or_create(
            name="Bibliotecario Zu",
            defaults={
                "backstory": "Ama los libros y disfruta compartir su conocimiento",
                "trait": "Reservado, amable",
                "interesting": "Le gusta leer y recomendar libros",
                "personality": "Paciente y observador",
                "is_friend": 20
            }
        )
        #Brad
        Character.objects.get_or_create(
            name="Brad",
            defaults={
                "backstory": "Ama jugar al futbool",
                "trait": "Energetico, amable",
                "interesting": "Le gusta jugar a la pelota y generalmente molestar",
                "personality": "Egocentrico pero pacifico",
                "is_friend": 20
            }
        )
        #Isabella
        Character.objects.get_or_create(
            name="Isabella",
            defaults={
                "backstory": "Ama pintar mucho y varias veces la fotografia",
                "trait": "Energetica, amable, divertida",
                "interesting": "Le gusta pintar mucho y pasar tiempo asolas",
                "personality": "Divertida, pacifica, tranquila y amable",
                "is_friend": 20
            }
        )
        #Sandro
        Character.objects.get_or_create(
            name="Sandro",
            defaults={
                "backstory": "Ama jugar Ajedrez por las noches se diria que sueña con el",
                "trait": "Energetica, amable, egocentrico, honrado, valiente",
                "interesting": "Le gusta mantenerse brillante como sus movimientos en ajedrez",
                "personality": "Divertido, pacifico, tranquilo y amable",
                "is_friend": 20
            }
        )
        #Pedro
        Character.objects.get_or_create(
            name="Pedro",
            defaults={
                "backstory": "Es bastante atletico",
                "trait": "Energetico",
                "interesting": "Le gusta hacer muchos deportes",
                "personality": "Energetica y fuerte",
                "is_friend": 20
            }
        )
        #Estafany
        Character.objects.get_or_create(
            name="Estefany",
            defaults={
                "backstory": "Risueña y divertida pero muy seria para el estudio",
                "trait": "Risueña",
                "interesting": "Le gusta estudiar se la pasa en la parte de estudio",
                "personality": "Estudiar y bailar",
                "is_friend": 20
            }
        )
        #Victor Joe
        Character.objects.get_or_create(
            name="Victor Joe",
            defaults={
                "backstory": "Es entrometido pero le encanta la musica",
                "trait": "Le gusta mucho la musica",
                "interesting": "Le gusta la musica y perderse en los libros y la musica",
                "personality": "Es amigable y socialmente agradable",
                "is_friend": 20
            }
        )

def create_situation_1_biblioteca(self):
    # Obtener personaje y locación
    bibliotecario = Character.objects.get(name="Bibliotecario")
    biblioteca = Location.objects.get(name="Biblioteca Central")

    # Crear situación del Día 1
    situation = Situations.objects.create(
        day=1,  # Día 1 = Situación 1
        title="Conflicto por el libro",
        location=biblioteca,
        main_character=bibliotecario,
        context="Came busca un libro de fantasía pero alguien más lo quiere también"
    )

    # Línea 1: Narración
    line1 = Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Mmmm parece ser la biblioteca central de la escuela, no es un mal lugar para pasar el tiempo...",
        order=1,
        is_decision_point=False
    )

    # Línea 2: Pensamiento de Came
    line2 = Dialogue.objects.create(
        situation=situation,
        line_type='came_thought',
        text="me pregunto si tendrán la nueva edición de Las aventuras por monje chino el antiguo Japon mediaval",
        order=2,
        is_decision_point=False
    )

    line3=Dialogue.objects.create(
        situation=situation,
        line_type='came_thought',
        text="me encantaría leer la nueva aventura de Sandra Martinez",
        order=3,
        is_decision_point=False
    )

    line4=Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Luego de un tiempo logra encontrar el libro porque se perdió luego de un tiempo",
        order=4,
        is_decision_point=False
    )

    line5=Dialogue.objects.create(
        situation=situation,
        line_type='came_thought',
        text="Lo tengo es mío por fin",
        order=5,
        is_decision_point=False
    )

    line6=Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Chocan sus manos con las de otra persona",
        order=6,
        is_decision_point=False
    )

    line7=Dialogue.objects.create(
        situation=situation,
        line_type='came_thought',
        text="me pregunto si tendrán la nueva edición de (nombre_libro)",
        order=7,
        is_decision_point=False
    )

    line8=Dialogue.objects.create(
        situation=situation,
        line_type='npc-speech',
        text="¿Quien eres y porque tocas mi libro?",
        order=8,
        is_decision_point=False
    )

    line9=Dialogue.objects.create(
        situation=situation,
        line_type='came-speech',
        text="Tu libro, yo lo vi primero es mío este libro",
        order=9,
        is_decision_point=False
    )

    line10=Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Came toma el libro y intenta huir pero lo toman de la espalda",
        order=10,
        is_decision_point=False
    )

    line11=Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Came toma el libro y intenta huir pero lo toman de la espalda",
        order=11,
        is_decision_point=False
    )

    line12=Dialogue.objects.create(
        situation=situation,
        line_type='narration',
        text="Came toma el libro y intenta huir pero lo toman de la espalda",
        order=12,
        is_decision_point=False
    )
    #Punto de decision
    decision_line=Dialogue.objects.create(
        situation=situation,
        line_type='npc-speech',
        text="Disculpa mis modales, me llamo Zu y me gusta si te das cuenta leer, y llevo mucho tiempo buscando este libro, salió hace poco y me emocione un poco al verlo, crees poder disculparme.",
        order=13,
        is_decision_point=True
    )

    # Opción 1: Buena
    choice1 = Choice.objects.create(
        dialogue_line=decision_line,
        text_choice="Aceptar las disculpas de Zu",
        consequence="Sí lo siento también es mi culpa por actuar así...",
        friendship_points=20,
        type_choice='buena',
        order=1
    )

    # Opción 2: Mala
    choice2 = Choice.objects.create(
        dialogue_line=decision_line,
        choice_text="Ignorar las disculpas de Zu",
        consequence_text="No las acepto pareces una mala persona",
        friendship_points=-20,
        choice_type='mala',
        order=2
    )