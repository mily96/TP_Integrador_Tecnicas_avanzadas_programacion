import pytest
from django.test import Client
from exam.models import Usuario




@pytest.mark.django_db
def test_usuario():

    client = Client()

    response = client.get('/api/v1/exam/usuarios/')

    assert response.status_code == 200


@pytest.fixture
def create_usuario():
    return Usuario(
        tipo="POSTULANTE",
        habilitado=True,
        nombre_usuario="mily",
        contrasenia="pass1234"
    )

@pytest.mark.django_db
def test_create_usuario_postulante(create_usuario):
    create_usuario.anteojos=False
    create_usuario.save()
    assert create_usuario.anteojos == False


@pytest.mark.django_db
def test_create_user_fail():
    with pytest.raises(Exception):
        Usuario.objects.create(
            anteojos=False,
            contrasenia="pass1234"
        )





