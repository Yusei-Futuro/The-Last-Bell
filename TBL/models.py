from random import choice

from django.db import models

# Create your models here.

class Username(models.Model):

    name = models.CharField(max_length=10)
    last_name = models.CharField (max_length=10)
    user = models.CharField( max_length=10)
    password = models.CharField( max_length=10)

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
