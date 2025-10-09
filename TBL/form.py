from importlib.metadata import requires

from django import forms
from django.forms import CharField


class Login(forms.Form):

    user= forms.CharField(label="Username", max_length=10)
    password= forms.CharField()

class Register(forms.Form):

    name=forms.CharField(label="Nombre", max_length=10)
    last_name=forms.CharField(label="Apellidos", max_length= 10)
    user=forms.CharField(label="Usuario", max_length=10)
    password=forms.CharField(label="Contraseña", max_length=10)
