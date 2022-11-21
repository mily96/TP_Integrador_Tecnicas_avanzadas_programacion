from rest_framework import viewsets


from .models import Examen, Pregunta
from .serializers import ExamenSerializer, PreguntaSerializer


class ExamenViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class PreguntaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer