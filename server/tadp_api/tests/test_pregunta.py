import pytest
from django.test import Client
from exam.models import Pregunta



@pytest.mark.django_db
def test_pregunta():

    client = Client()

    response = client.get('/api/v1/exam/preguntas/')

    assert response.status_code == 200


@pytest.fixture
def create_pregunta():
    return Pregunta(
        descripcion="¿En qué circunstancia está permitido circular sin respetar distancias prudentes con el vehículo que va adelante?"
    )

@pytest.mark.django_db
def test_create_pregunta(create_pregunta):
    create_pregunta.save()
    assert create_pregunta.descripcion == "¿En qué circunstancia está permitido circular sin respetar distancias prudentes con el vehículo que va adelante?"

