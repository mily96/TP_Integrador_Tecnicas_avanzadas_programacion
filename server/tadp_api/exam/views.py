from django.shortcuts import render
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
from rest_framework import generics
from .serializers import (
    OpcionSerializer,
    PreguntaSerializer,
    UsuarioSerializer,
    ClaveSerializer,
    TurnoExamenSerializer,
    TurnoRevisionSerializer,
    ExamenSerializer,
    PreguntaOpcionSerializer,
    RespuestaSerializer
)

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
    
# Usuario Views

class UsuarioCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Usuario
    queryset = Usuario.objects.all(),
    serializer_class = UsuarioSerializer

class UsuarioList(generics.ListAPIView):
    # API endpoint that allows Usuario to be viewed.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Usuario by pk.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Usuario record to be updated.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
class UsuarioDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Usuario record to be deleted.
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
# Clave Views

class ClaveCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Clave
    queryset = Clave.objects.all(),
    serializer_class = ClaveSerializer

class ClaveList(generics.ListAPIView):
    # API endpoint that allows Clave to be viewed.
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer

class ClaveDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Clave by pk.
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer
    
class ClaveUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Clave record to be updated.
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer
    
class ClaveDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Clave record to be deleted.
    queryset = Clave.objects.all()
    serializer_class = ClaveSerializer
    
# TurnoExamen Views

class TurnoExamenCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new TurnoExamen
    queryset = TurnoExamen.objects.all(),
    serializer_class = TurnoExamenSerializer

class TurnoExamenList(generics.ListAPIView):
    # API endpoint that allows TurnoExamen to be viewed.
    queryset = TurnoExamen.objects.all()
    serializer_class = TurnoExamenSerializer

class TurnoExamenDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single TurnoExamen by pk.
    queryset = TurnoExamen.objects.all()
    serializer_class = TurnoExamenSerializer
    
class TurnoExamenUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a TurnoExamen record to be updated.
    queryset = TurnoExamen.objects.all()
    serializer_class = TurnoExamenSerializer
    
class TurnoExamenDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a TurnoExamen record to be deleted.
    queryset = TurnoExamen.objects.all()
    serializer_class = TurnoExamenSerializer

# TurnoRevision Views

class TurnoRevisionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new TurnoRevision
    queryset = TurnoRevision.objects.all(),
    serializer_class = TurnoRevisionSerializer

class TurnoRevisionList(generics.ListAPIView):
    # API endpoint that allows TurnoRevision to be viewed.
    queryset = TurnoRevision.objects.all()
    serializer_class = TurnoRevisionSerializer

class TurnoRevisionDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single TurnoRevision by pk.
    queryset = TurnoRevision.objects.all()
    serializer_class = TurnoRevisionSerializer
    
class TurnoRevisionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a TurnoRevision record to be updated.
    queryset = TurnoRevision.objects.all()
    serializer_class = TurnoRevisionSerializer
    
class TurnoRevisionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a TurnoRevision record to be deleted.
    queryset = TurnoRevision.objects.all()
    serializer_class = TurnoRevisionSerializer

# Examen Views

class ExamenCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Examen
    queryset = Examen.objects.all(),
    serializer_class = ExamenSerializer

class ExamenList(generics.ListAPIView):
    # API endpoint that allows Examen to be viewed.
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer

class ExamenDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Examen by pk.
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    
class ExamenUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Examen record to be updated.
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    
class ExamenDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Examen record to be deleted.
    queryset = Examen.objects.all()
    serializer_class = ExamenSerializer
    
# PreguntaOpcion Views

class PreguntaOpcionCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new PreguntaOpcion
    queryset = PreguntaOpcion.objects.all(),
    serializer_class = PreguntaOpcionSerializer

class PreguntaOpcionList(generics.ListAPIView):
    # API endpoint that allows PreguntaOpcion to be viewed.
    queryset = PreguntaOpcion.objects.all()
    serializer_class = PreguntaOpcionSerializer

class PreguntaOpcionDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single PreguntaOpcion by pk.
    queryset = PreguntaOpcion.objects.all()
    serializer_class = PreguntaOpcionSerializer
    
class PreguntaOpcionUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a PreguntaOpcion record to be updated.
    queryset = PreguntaOpcion.objects.all()
    serializer_class = PreguntaOpcionSerializer
    
class PreguntaOpcionDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a PreguntaOpcion record to be deleted.
    queryset = PreguntaOpcion.objects.all()
    serializer_class = PreguntaOpcionSerializer

# Respuesta Views

class RespuestaCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new Respuesta
    queryset = Respuesta.objects.all(),
    serializer_class = RespuestaSerializer

class RespuestaList(generics.ListAPIView):
    # API endpoint that allows Respuesta to be viewed.
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer

class RespuestaDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single Respuesta by pk.
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    
class RespuestaUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a Respuesta record to be updated.
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer
    
class RespuestaDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a Respuesta record to be deleted.
    queryset = Respuesta.objects.all()
    serializer_class = RespuestaSerializer