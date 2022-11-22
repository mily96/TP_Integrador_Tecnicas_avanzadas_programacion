from django.urls import include, path
from .views import (
    OpcionCreate,
    OpcionList,
    OpcionDetail,
    OpcionUpdate,
    OpcionDelete,
    PreguntaCreate,
    PreguntaList,
    PreguntaDetail,
    PreguntaUpdate,
    PreguntaDelete
)

urlpatterns = [
    path('opcion/create/', OpcionCreate.as_view(), name='create-opcion'),
    path('opciones/', OpcionList.as_view()),
    path('opcion/<int:pk>/', OpcionDetail.as_view(), name='retrieve-opcion'),
    path('opcion/update/<int:pk>/', OpcionUpdate.as_view(), name='update-opcion'),
    # path('opcion/delete/<int:pk>/', OpcionDelete.as_view(), name='delete-opcion')
    path('pregunta/create/', PreguntaCreate.as_view(), name='create-pregunta'),
    path('preguntas/', PreguntaList.as_view()),
    path('pregunta/<int:pk>/', PreguntaDetail.as_view(), name='retrieve-pregunta'),
    path('pregunta/update/<int:pk>/', PreguntaUpdate.as_view(), name='update-pregunta'),
    # path('pregunta/delete/<int:pk>/', PreguntaDelete.as_view(), name='delete-pregunta')
]