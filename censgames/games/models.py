from django.db import models

# Create your models here.

class Jogo(models.Model):

    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    genero = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    plataforma = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    email = models.CharField(
        max_length=150,
        null=False,
        blank=False
    )


