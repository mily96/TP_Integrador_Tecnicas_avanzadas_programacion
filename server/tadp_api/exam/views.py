from django.shortcuts import render
from .models import Pregunta
from rest_framework import generics
from .serializers import PreguntaSerializer

# Pregunta Views

class PreguntaCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Pregunta
    queryset = Pregunta.objects.all(),
    serializer_class = PreguntaSerializer

class PreguntaList(generics.ListAPIView):
    # API endpoint that allows Pregunta to be viewed.
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer

class PreguntaDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Pregunta by pk.
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    
class PreguntaUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Pregunta record to be updated.
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer
    
class PreguntaDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Pregunta record to be deleted.
    queryset = Pregunta.objects.all()
    serializer_class = PreguntaSerializer