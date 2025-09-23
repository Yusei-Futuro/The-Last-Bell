from django.db import models

# Create your models here.
class User(models.Model):
    #Campos importantes sobre letras
    nombre_user=models.CharField(max_length=10)
    email_user=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)


