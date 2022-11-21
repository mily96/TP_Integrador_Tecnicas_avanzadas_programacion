from django.db import models



#Defino la clase Examen
class Examen(models.Model):
    id = models.IntegerField(primary_key=True)
    fecha = models.DateField(auto_now_add=True) #Guarda la fecha de hoy
    duracion = models.IntegerField()
    realizado = models.BooleanField()

#Defino la clase Pregunta
class Pregunta(models.Model):
    id_pregunta = models.IntegerField(primary_key=True)
    descripcion = models.TextField()
    opcion_uno = models.CharField(max_length=100)
    opcion_dos = models.CharField(max_length=100)
    opcion_tres = models.CharField(max_length=100)
    opcion_correcta = models.CharField(max_length=100)
