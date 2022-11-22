from rest_framework import serializers
from .models import (Opcion, Pregunta)

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregunta 
        fields = ['id_pregunta', 'descripcion']
        
        
class OpcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opcion 
        fields = ['id_opcion', 'descripcion']