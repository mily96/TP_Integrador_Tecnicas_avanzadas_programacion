from django.shortcuts import render
from .models import (Opcion, Pregunta)
from rest_framework import generics
from .serializers import (OpcionSerializer, PreguntaSerializer)

# Opcion Views

class OpcionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Opcion
    queryset = Opcion.objects.all(),
    serializer_class = OpcionSerializer

class OpcionList(generics.ListAPIView):
    # API endpoint that allows Opcion to be viewed.
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

class OpcionDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Opcion by pk.
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    
class OpcionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Opcion record to be updated.
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer
    
class OpcionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Opcion record to be deleted.
    queryset = Opcion.objects.all()
    serializer_class = OpcionSerializer

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