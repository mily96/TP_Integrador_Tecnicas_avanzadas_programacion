# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    tipo = models.TextField()
    habilitado = models.BooleanField()
    anteojos = models.BooleanField()
    nombre_usuario = models.TextField()
    contrasenia = models.TextField()

    class Meta:
        db_table = 'usuario'

class Clave(models.Model):
    id_clave = models.AutoField(primary_key=True)
    valor = models.TextField()
    fecha_creacion = models.DateField()
    es_valida = models.BooleanField()

    class Meta:
        db_table = 'clave'


class Examen(models.Model):
    id_examen = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_clave = models.ForeignKey(Clave, models.DO_NOTHING, db_column='id_clave')
    fecha = models.DateField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    realizado = models.BooleanField()

    class Meta:
        db_table = 'examen'


class Opcion(models.Model):
    id_opcion = models.AutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        db_table = 'opcion'


class Pregunta(models.Model):
    id_pregunta = models.AutoField(primary_key=True)
    descripcion = models.TextField()

    class Meta:
        db_table = 'pregunta'


class PreguntaOpcion(models.Model):
    id_pregunta = models.OneToOneField(Pregunta, models.DO_NOTHING, db_column='id_pregunta', related_name="pregunta", primary_key=True)
    id_opcion = models.ForeignKey(Opcion, models.DO_NOTHING, db_column='id_opcion', related_name="opcion")
    opcion_correcta = models.BooleanField()

    class Meta:
        db_table = 'pregunta_opcion'
        unique_together = (('id_pregunta', 'id_opcion'),)


class Respuesta(models.Model):
    id_examen = models.OneToOneField(Examen, models.DO_NOTHING, db_column='id_examen', primary_key=True)
    id_pregunta = models.ForeignKey(PreguntaOpcion, models.DO_NOTHING, db_column='id_pregunta')
    id_opcion = models.IntegerField()

    class Meta:
        db_table = 'respuesta'
        unique_together = (('id_examen', 'id_pregunta', 'id_opcion'),)


class TurnoExamen(models.Model):
    id_turno_examen = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()

    class Meta:
        db_table = 'turno_examen'


class TurnoRevision(models.Model):
    id_turno_revision = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    fecha = models.DateField()

    class Meta:
        db_table = 'turno_revision'



