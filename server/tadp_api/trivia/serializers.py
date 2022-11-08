from rest_framework import serializers

#from .models import Question, Answer
from .models import Examen

#class AnswerSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Answer
#        fields = ['answer', 'is_correct']

#class QuestionSerializer(serializers.ModelSerializer):
#    answers = AnswerSerializer(many=True, read_only=True)

#    class Meta:
#        model = Question
#        fields = ['category', 'question', 'answers']


class ExamenSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    fecha = serializers.DateField() 
    duracion = serializers.IntegerField()
    realizado = serializers.BooleanField()