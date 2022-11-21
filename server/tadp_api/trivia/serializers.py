from rest_framework import serializers


from .models import Examen, Pregunta


class ExamenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    fecha = serializers.DateField() 
    duracion = serializers.IntegerField()
    realizado = serializers.BooleanField()

    class Meta:
        model = Examen
        fields = ['id', 'fecha', 'duracion', 'realizado']

class PreguntaSerializer(serializers.ModelSerializer):
    id_pregunta = serializers.IntegerField()
    descripcion = serializers.CharField()
    opcion_uno = serializers.CharField()
    opcion_dos = serializers.CharField()
    opcion_tres = serializers.CharField()
    opcion_correcta = serializers.CharField()

    class Meta:
        model = Pregunta
        fields = ['id_pregunta', 'descripcion', 'opcion_uno', 'opcion_dos', 'opcion_tres', 'opcion_correcta']