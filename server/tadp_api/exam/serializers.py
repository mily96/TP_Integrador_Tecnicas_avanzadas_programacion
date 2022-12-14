from rest_framework import serializers
from .models import (
    Clave,
    Examen,
    Opcion,
    Pregunta,
    PreguntaOpcion,
    Respuesta,
    TurnoExamen,
    TurnoRevision,
    Usuario
)

class OpcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Opcion 
        fields = ['id_opcion', 'descripcion']

class PreguntaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pregunta 
        fields = ['id_pregunta', 'descripcion']
        
class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuario 
        fields = [
            'id_usuario',
            'tipo',
            'habilitado',
            'anteojos',
            'nombre_usuario',
            'contrasenia'
        ]

class ClaveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clave 
        fields = [
            'id_clave',
            'valor',
            'fecha_creacion',
            'es_valida'
        ]
        
class TurnoExamenSerializer(serializers.ModelSerializer):

    class Meta:
        model = TurnoExamen 
        fields = [
            'id_turno_examen',
            'id_usuario',
            'fecha'
        ]

class TurnoRevisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TurnoRevision 
        fields = [
            'id_turno_revision',
            'id_usuario',
            'fecha'
        ]

class ExamenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Examen 
        fields = [
            'id_examen',
            'id_usuario',
            'id_clave',
            'fecha',
            'duracion',
            'realizado'
        ]
        
class PreguntaOpcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PreguntaOpcion 
        fields = [
            'id_pregunta',
            'id_opcion',
            'opcion_correcta'
        ]
        
class RespuestaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Respuesta 
        fields = [
            'id_examen',
            'id_pregunta',
            'id_opcion'
        ]

# Custom Serializers
class PreguntasDetailSerializer(serializers.ModelSerializer):
    id_pregunta = PreguntaSerializer(required=True)
    id_opcion = OpcionSerializer(required=True)

    class Meta:
        model = PreguntaOpcion
        fields = ('id_pregunta', 'id_opcion', 'opcion_correcta')

    def create(self, validated_data):
        pregunta_data = validated_data.pop('id_pregunta')
        opcion_data = validated_data.pop('id_opcion')
        pregunta = PreguntaSerializer.create(PreguntaSerializer(), validated_data=pregunta_data)
        opcion = OpcionSerializer.create(OpcionSerializer(), validated_data=opcion_data)
        pregunta_detail = PreguntaOpcion.objects.update_or_create(id_pregunta=pregunta,id_opcion=opcion,
                            opcion_correcta=validated_data.pop('opcion_correcta'))
        return pregunta_detail