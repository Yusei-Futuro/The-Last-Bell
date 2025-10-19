from random import choice
from tkinter.constants import CASCADE

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
    trait = models.CharField(max_length=100)  # Ej: "Autista", "Migrante", "No binarie"
    image_url = models.URLField(blank=True)

class Dialogue(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    text = models.TextField()
    decision_point = models.BooleanField(default=False)

class Choice(models.Model):
    dialogue = models.ForeignKey(Dialogue, on_delete=models.CASCADE, related_name="choice_from")
    text = models.CharField(max_length=200)
    consequence = models.TextField()
    next_dialogue = models.ForeignKey(Dialogue, on_delete=models.SET_NULL, null=True, blank=True,related_name="choice_to")
