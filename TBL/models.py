from random import choice
from tkinter.constants import CASCADE
from tkinter.font import names

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Username(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Username"
    )
    player_name=models.CharField(
        max_length=50,
        default="Kove",
        help_text="Nombre a su jugador"
    )
    select_conditions=models.CharField(
        max_length=50,
        default="TEA",
        choices=[
            ('TEA', 'Trastorno del Espectro Autista'),
            ('DOWN', 'Síndrome de Down'),
            ('ADHD', 'TDAH'),
            ('OTHER', 'Otra'),
        ],
        help_text="Seleccione la condicion de su personaje (default:TEA)"
    )
    situation=models.IntegerField(
        default=1,
        help_text="Primera situacion del game"
    )
    situation_complet=models.BooleanField(
        default=False,
        help_text="Cuando complete la sitaucion del primer dia"

    )
    friend=models.IntegerField(

        default=0,
        help_text="Cantidad de amigos"
    )
    friend_counts=models.IntegerField(
        default=0,
        help_text="Cantidad de amigos al final"
    )
    final=models.BooleanField(
        default=False,
        help_text="Cuando completo todos los dias es TRUE"
    )

    class Meta:
        verbose_name="Perfil de jugador"
        verbose_name_plural="Perfiles de jugadores"

    def __str__(self):
        return f"{self.user.username} - Día {self.situation}"

    def calculate_friends(self):

        self.friend_counts = self.npc_relationships.filter(is_friend=True).count()
        self.save()

        return self.friend_counts

    def advance_to_next_day(self):

        if self.situation_complet and self.situation < 7:
            self.situation += 1
            self.situation_complet = False
            self.save()

        elif self.situation >= 7:
            self.final = True
            self.save()

class Location(models.Model):
    locations=models.CharField(
        max_length=50,
        unique=True,
        help_text="Nombre de la location"
    )
    descriptions=models.TextField(
        max_length=500,
        help_text="Descripcion de la situacion al llegar al juego"
    )
    imagen_fondo=models.URLField(

        blank=True,
        null=True,
        help_text="URl de las imagenes"
    )
    day_location=models.IntegerField(
        default=1,
        help_text="Asignacion de las situaciones"
    )
    class Meta:

        verbose_name = "Locación"
        verbose_name_plural = "Locaciones"
        ordering = ["day_location", "locations"]

    def __str__(self):
        return f"{self.locations} (Día {self.day_location})"

class Character(models.Model):
    name = models.CharField(max_length=100)
    backstory = models.TextField()
    trait = models.CharField(max_length=100)
    image_url = models.URLField(
        blank=True,
        null=True,
                                )
    interesting=models.TextField(
        help_text="Intereses del personaje para abordar mas la historia"
    )

    personality=models.TextField(
        help_text="Personalidad"
    )
    is_friend=models.IntegerField(
        default=20,
        help_text="Puntos necesarios para considerarse amigo"
    )

    class Meta:
        verbose_name="Personaje"
        verbose_name_plural="Personajes"
        ordering=["name"]

    def __str__(self):
        return self.name

class Prologo(models.Model):

    title=models.CharField(
        max_length=200,
        default="El comienzo de una nueva vida",
        help_text="Para el titulo del juego"
    )

    orden=models.IntegerField(
        unique=True,
        help_text="Aca quiero lo del orden de aparacion de la cinematicas"
    )

    text_prologo=models.TextField(
        help_text="Texto que aparecera en la pantalla"
    )

    content_dialogue=models.CharField(
        max_length=200,  #Faltan aca escribir los dialogos ok lo dejare expresado
        choices=[
            ('narration', 'Narración'),
            ('dialogue', 'Diálogo (Mamá, Álex, etc.)'),
            ('came_thought', 'Pensamiento de Came'),
        ]
    )

    character = models.ForeignKey(
        'Character',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Personaje que habla (si es diálogo)"
    )

    class Meta:
        verbose_name = "Prólogo"
        verbose_name_plural = "Prólogos"
        ordering = ['orden']

    def __str__(self):
        return f"Prólogo {self.orden}: {self.content_dialogue()}"

class Situations(models.Model):
    title=models.CharField(
        max_length=20,
        help_text="Nombre de la situacion"
    )

    day=models.IntegerField(
        unique=True,
        help_text="Numero de situacion en la que me encuentro"
    )

    locations=models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name="situations"
    )

    character=models.ForeignKey(
        Character,
        on_delete=models.CASCADE,
        related_name="situations",
        blank=True,
        null=True
    )

    contexto_situation=models.TextField(
        help_text="Para hacer el contexto de la situacion en la que se encuentra"
    )

    is_gameplay=models.BooleanField(
        default=True,
        help_text="Campo para saber si es jugable"
    )

    orden_dialogue=models.IntegerField(
        default=0,
        help_text="Lineas de dialogo del day"
    )

    class Meta:
        verbose_name = "Situación"
        verbose_name_plural = "Situaciones"
        ordering = ['day']

    def __str__(self):
        return f"Día {self.day}: {self.title}"

class Dialogue(models.Model):

    TYPE_CHOICES = [
        ('narration', 'Narración'),
        ('came_thought', 'Pensamiento de Came (Came*:)'),
        ('came_speech', 'Came habla'),
        ('npc_speech', 'NPC habla'),
        ('system', 'Mensaje del sistema'),
    ]

    character = models.ForeignKey(Character,
                                  on_delete=models.CASCADE,
                                  null=True,
                                  blank=True,
                                  related_name="dialogue_lines"
                                               )

    situation=models.ForeignKey(Situations,
                               on_delete=models.CASCADE,
                               related_name="dialogue_lines"
                               )

    text = models.TextField(
        help_text="Para saber el dialogo"
    )

    decision_point = models.BooleanField(
        default=False,
        help_text="Para comprobar si lo de alante es un dialogo o no"
    )

    lines_type= models.CharField(
        max_length=200,
        choices=TYPE_CHOICES
    )

    orden= models.IntegerField(
        help_text="Orden en que aparecen en la linea de texto"
    )

    class Meta:
        verbose_name = "Línea de Diálogo"
        verbose_name_plural = "Líneas de Diálogo"
        ordering = ['situation', 'orden']

    def __str__(self):
        return f"{self.situation} - Línea {self.orden}: {self.get_line_type_display()}"

class Choice(models.Model):

    CHOICE_TYPE_CHOICES = [
        ('buena', 'Decisión Buena'),
        ('mala', 'Decisión Mala'),
        ('intermedia', 'Decisión Intermedia'),
        ('neutral', 'Decisión Neutral'),
    ]

    dialogue = models.ForeignKey(
        Dialogue,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    text_choice=models.CharField(
        max_length=300
    )

    consequence = models.TextField(
        help_text="para saber que pasa despues"
    )

    order = models.IntegerField(
        default=0,
    )

    next_dialogue = models.ForeignKey(
        Dialogue,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="choice"
    )

    type_choice=models.CharField(
        max_length=20,
        choices=CHOICE_TYPE_CHOICES
    )

    friendship_points = models.IntegerField(
        default=0,
        help_text="Puntos que suma/resta a la relación con el NPC (+10 buena, -5 mala, 0 neutral)"
    )

    class Meta:
        verbose_name = "Opción de Decisión"
        verbose_name_plural = "Opciones de Decisión"
        ordering = ['dialogue', 'order']

    def __str__(self):
        return f"{self.text_choice[:50]} ({self.type_choice})"

class History_Choice(models.Model):

    player=models.ForeignKey(
        Username,
        on_delete=models.CASCADE,
        related_name="history",
    )

    choice=models.ForeignKey(
        Choice,
        on_delete=models.CASCADE,
        related_name="history"
    )

    situation=models.ForeignKey(
        Situations,
        on_delete=models.CASCADE
    )

    day=models.IntegerField(
        help_text="Para saber cuando tomo las decisiones"
    )

    points_earned = models.IntegerField(
        help_text="Puntos de amistad que ganó/perdió con esta decisión"
    )

    class Meta:
        verbose_name = "Historial de Decisión"
        verbose_name_plural = "Historial de Decisiones"
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.player.user.username} - Día {self.day}: {self.choice.text_choice[:30]}"

#Preguntar a mi papa si es necesario un modelo sobre NPCrelation

class GameSave(models.Model):

    perfil=models.ForeignKey(
        Username,
        on_delete=models.CASCADE,
        related_name="gamesave"
    )