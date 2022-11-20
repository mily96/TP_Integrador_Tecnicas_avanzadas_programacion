from django.db import models



#Defino la clase Examen
class Examen(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now_add=True) #Guarda la fecha de hoy
    duracion = models.IntegerField()
    realizado = models.BooleanField()
