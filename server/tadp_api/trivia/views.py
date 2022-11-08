from rest_framework import viewsets

#from .models import Question, Examen
from .models import Examen
#from .serializers import QuestionSerializer
from .serializers import ExamenSerializer

#class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
#    queryset = Question.objects.all()
#    serializer_class = QuestionSerializer

class ExamenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer