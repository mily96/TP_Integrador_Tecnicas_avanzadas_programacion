from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from trivia import views

router = routers.DefaultRouter()
#router.register(r'examen', views.ExamenViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('examen/', include(router.urls)), #URL de examen
    #path('',include(router.urls),name="Examen") #URL de examen
]