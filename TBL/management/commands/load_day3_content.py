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
            contexto_situation="Parece que para ser bastante popular está solita, podríamos intentar acompañarla. Creo que no me haría mal tener una amiga."
        )

        line1 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Parece que todas las mesas están ocupadas, bueno buscaré el sitio más alejado posible.", order=1, decision_point=False)
        line2 = Dialogue.objects.create(situation=situation, line_type='narration', text="Came se sienta al lado de una chica sin darse cuenta, empieza a pensar que puede ser que la esté incomodando.", order=2, decision_point=False)
        line3 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="Bueno voy a empezar con un 'Hola'", order=3, decision_point=False)
        line4 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Hola", order=4, decision_point=False)
        line5 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="… Me llamo Came … un gusto", order=5, decision_point=False)
        line6 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_thought', text="*Lo mira confundida*", order=6, decision_point=False)
        line7 = Dialogue.objects.create(situation=situation, character=came, line_type='came_thought', text="¿Por qué me mira así? ¿Hice algo mal?", order=7, decision_point=False)
        line8 = Dialogue.objects.create(situation=situation, line_type='narration', text="Came se intenta levantar e irse, pero Lisa le sonríe.", order=8, decision_point=False)
        line9 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Mucho gusto, mi nombre es Lisa.", order=9, decision_point=False)
        line10 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="*risas* porque te sentaste por acá", order=10, decision_point=False)
        line11 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Parece ser que no había espacio por el lugar, lo siento si te incomodé.", order=11, decision_point=False)
        line12 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="No te preocupes, yo también quería escapar un poco del ruido en el centro.", order=12, decision_point=False)
        line13 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="¿Por qué?", order=13, decision_point=False)
        line14 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="Es que me gusta pintar y con tanto ruido no consigo del todo concentrarme y…", order=14, decision_point=False)
        line15 = Dialogue.objects.create(situation=situation, character=came, line_type='came_speech', text="Son todas aburridas.", order=15, decision_point=False)
        line16 = Dialogue.objects.create(situation=situation, character=npc, line_type='npc_speech', text="*risas* exacto, y me encanta dibujar.", order=16, decision_point=False)
        
        decision_line = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="¿Te gusta dibujar mucho entonces?",
            order=17,
            decision_point=True
        )

# Ruta mala
        line21 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="No me parece divertido dibujar.",
            order=18,
            decision_point=False
        )

        line22 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="*Se queda confundida*",
            order=19,
            decision_point=False
        )

        line23 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_thought',
            text="¿Por qué me dice eso? Será que fui muy intensa de una manera u otra.",
            order=20,
            decision_point=False
        )

        line24 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="Ok, entiendo … te puedes ir entonces.",
            order=21,
            decision_point=False
        )

        line25 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_thought',
            text="Porque se habrá enojado, no consigo comprenderlo del todo.",
            order=22,
            decision_point=False
        )

        line26 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Came se gira y se despide, aunque sabe que probablemente nunca la volverá a ver.",
            order=23,
            decision_point=False
        )

# Ruta buena - Gap para separar rutas
        line18 = Dialogue.objects.create(
            situation=situation,
            character=came,
            line_type='came_speech',
            text="¡Sí! Me encanta dibujar.",
            order=30,
            decision_point=False
        )

        line19 = Dialogue.objects.create(
            situation=situation,
            character=npc,
            line_type='npc_speech',
            text="La verdad es que es mi pasión.",
            order=31,
            decision_point=False
        )

        line20 = Dialogue.objects.create(
            situation=situation,
            line_type='narration',
            text="Pasaron el recreo hablando sobre diferentes obras de arte, Came escuchaba aunque a veces se quedaba un segundo en las nubes, pero Lisa le daba golpes para que volviera al mundo.",
            order=32,
            decision_point=False
        )

        # Crear choices con next_dialogue
        choice_buena = Choice.objects.create(
            dialogue=decision_line,
            text_choice="Sí, me encanta dibujar.",
            consequence="¡Qué genial! Pasamos el recreo hablando sobre obras de arte y compartiendo ideas.",
            friendship_points=20,
            type_choice='buena',
            order=1,
            next_dialogue=line18
        )

        choice_mala = Choice.objects.create(
            dialogue=decision_line,
            text_choice="No me parece divertido dibujar.",
            consequence="Se quedó confundida, parece molesta. Came se retira.",
            friendship_points=-20,
            type_choice='mala',
            order=2,
            next_dialogue=line21
        )