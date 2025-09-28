from django.db import models

# Create your models here.

class Username(models.Model):

    name = models.CharField(max_length=10)
    last_name = models.CharField (max_length=10)
    user = models.CharField( max_length=10)
    password = models.CharField( max_length=10)


