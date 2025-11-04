from django.core.management.base import BaseCommand
from TBL.models import Character, Location, Situations, Dialogue, Choice

class Command(BaseCommand):
    help = 'Carga el contenido del Dia 4 desde dialogos.txt'

    def handle(self, *args, **kwargs):
        self.create_characters()
        self.create_locations()
        self.create_situation()
        self.stdout.write(self.style.SUCCESS("Dia 4 del juego cargado correctamente"))

    def create_characters(self):
        Character.objects.get_or_create(
            name="Came",
            defaults={ 
                "backstory": "Se mudó a una nueva ciudad recientemente...",
                "interesting": "Leer y conocer nuevos lugares",
                "personality": "Amable, un poco tímido",
                "is_friend": 20
            }
        )

        Character.objects.get_or_create(
            name="Alicie",
            defaults={
                "backstory": "Le gusta la música y conocer gente nueva.",
                "interesting": "Tocar la batería",
                "personality": "Sociable y simpática",
                "is_friend": 20,
                "image_url": "game_characters/npc-4.png"
            }
        )

    def create_locations(self):
        Location.objects.get_or_create(
            locations="Plaza",
            defaults={
                "descriptions": "Un lugar abierto con áreas verdes, personas conversando y jugando alrededor.",
                "imagen_fondo": "game_locations/plaza.jpg"
            }
        )

    def create_situation(self):
        came = Character.objects.get(name="Came")
        npc = Character.objects.get(name="Alicie")
        plaza = Location.objects.get(locations="Plaza")

        situation = Situations.objects.create(
            day=4,
            title="Una conexión musical",
            locations=plaza,
            character=npc,
            contexto_situation="Came está escuchando su música en una playlist de Spotify. A su alrededor hay personas conversando y jugando, hasta que alguien se le acerca."
        )

        line1 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Esta música está muy buena", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, character=came, line_type='came_action', text="Le da like para tenerla guardada en la playlist", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Hola, ¿qué tal? ¿Qué música escuchas?", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Holaaa, estoy escuchando rock alternativo, me gusta mucho ese tipo de música", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="A propósito, me llamo Came", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="A lo siento por no presentarme, me llamo Alicie", order=6, decision_point=False)
        line7 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="A propósito, ¿tienes alguna banda favorita?", order=7, decision_point=False)
        line8 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Últimamente escucho mucho Tame Impala y Arctic Monkeys. ¿A ti qué te gusta?", order=8, decision_point=False)
        line9 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Me gusta también ese tipo de rock, pero me atrae el rock español, por ejemplo Soda Stereo, Los Prisioneros, Los Tres, entre otros.", order=9, decision_point=False)
        line10 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="¿Te gustaría que nos compartamos las playlists?", order=10, decision_point=False)

        decision_line = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Claro, no tengo problema. ¿Tocas instrumentos? Podríamos hacer un cover de alguna canción de un grupo que nos guste.",
            order=11,
            decision_point=True
        )

        # Ruta mala
        line12 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Mmm, no lo sé, en general no comparto mis playlists.",
            order=12,
            decision_point=False
        )

        line13 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Las hago solamente para mí.",
            order=13,
            decision_point=False
        )

        line14 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Ok, está bien, lo entiendo.",
            order=14,
            decision_point=False
        )

        line15 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Igual te podría pasar algunas canciones pero no las playlists.",
            order=15,
            decision_point=False
        )

        line16 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Está bien, no hay problema.",
            order=16,
            decision_point=False
        )

        line17 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Aunque la relación se corta rápidamente, Came rechaza la situación de forma suave y no se abre del todo.",
            order=17,
            decision_point=False
        )

# Ruta buena
        line18 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Claro, no tengo problema. ¿Tocas instrumentos? Podríamos hacer un cover de alguna canción que nos guste.",
            order=30,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Obvio, toco la batería, soy bueno en eso.",
            order=31,
            decision_point=False
        )

        line20 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="Excelente, también podemos juntar más gente y formar un grupo, puede ser solo por hobby.",
            order=32,
            decision_point=False
        )

        line21 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Me parece estupendo.",
            order=33,
            decision_point=False
        )

        line22 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="De esta forma, Came y Alicie conectan y planean tocar juntos, iniciando una nueva amistad basada en la música.",
            order=34,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Aceptar compartir playlists y tocar música juntos",
            consequence="Came se muestra entusiasmado por la idea de formar un grupo y compartir música.",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line18
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="No compartir playlists",
            consequence="Came prefiere no abrirse demasiado, aunque lo hace de forma educada.",
            friendship_points=-20,
            type_choice='mala',
            order=2,
            next_dialogue=line12
        )

