import pytest
from django.test import Client
from exam.models import Usuario, Examen, Clave



@pytest.mark.django_db
def test_examen():

    client = Client()

    response = client.get('/api/v1/exam/examenes/')

    assert response.status_code == 200


@pytest.mark.django_db
def test_create_examen():
    usr = Usuario.objects.create(
        tipo="POSTULANTE",
        habilitado=True,
        anteojos=False,
        nombre_usuario="andres",
        contrasenia="pass1234"
    )
    clave = Clave.objects.create(
        valor="clave de prueba",
        fecha_creacion="2022-11-22",
        es_valida=True
    )
    exam = Examen.objects.create(
        id_usuario = usr,
        fecha="2022-11-22",
        duracion=60,
        id_clave=clave,
        realizado=True
    )
    assert exam.fecha == "2022-11-22"

@pytest.mark.django_db
def test_create_examen_fail():
    with pytest.raises(Exception):
        Examen.objects.create(
            id_usuario = usr,
            fecha="2022-11-22",
            id_clave=clave,
            realizado=True
        )