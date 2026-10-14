from pyclbr import Class

from django.db import models

#Crear un modelo para Equipo y Arriendo y cada resgitro asociado a un equipo.

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_adquisicion = models.DateField()
    estado = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Arriendo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"Arriendo de {self.equipo.nombre} para {self.cliente}"
