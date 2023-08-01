from django.db import models

class Mascota(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    especie = models.CharField(max_length=100)

class Reptil(Mascota):
    tipo_escamas = models.CharField(max_length=100)

class Ave(Mascota):
    tipo_plumaje = models.CharField(max_length=100)

class Anfibio(Mascota):
    tipo_piel = models.CharField(max_length=100)
