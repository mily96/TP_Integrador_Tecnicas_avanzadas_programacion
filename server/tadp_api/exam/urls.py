from django.urls import include, path
from .views import (
    PreguntaCreate,
    PreguntaList,
    PreguntaDetail,
    PreguntaUpdate,
    PreguntaDelete
)

urlpatterns = [
    path('pregunta/create/', PreguntaCreate.as_view(), name='create-pregunta'),
    path('preguntas/', PreguntaList.as_view()),
    path('pregunta/<int:pk>/', PreguntaDetail.as_view(), name='retrieve-pregunta'),
    path('pregunta/update/<int:pk>/', PreguntaUpdate.as_view(), name='update-pregunta'),
    # path('pregunta/delete/<int:pk>/', PreguntaDelete.as_view(), name='delete-pregunta')
]