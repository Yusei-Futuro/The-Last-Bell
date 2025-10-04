from django.contrib import admin
from .models import Character, Dialogue, Choice

# Register your models here.

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('name', 'trait')
    search_fields = ('name', 'trait')
    ordering = ('name',)

@admin.register(Dialogue)
class DialogueAdmin(admin.ModelAdmin):
    list_display = ('character', 'text', 'decision_point')
    list_filter = ('decision_point',)
    search_fields = ('text',)
    autocomplete_fields = ['character']

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('dialogue', 'text', 'next_dialogue')
    search_fields = ('text', 'consequence')
    autocomplete_fields = ['dialogue', 'next_dialogue']