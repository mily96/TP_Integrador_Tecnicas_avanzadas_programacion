from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from trivia import views

schema_view = get_schema_view(
   openapi.Info(
      title="TADP API",
      default_version='v1',
      description="TADP API",
      terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'preguntas', views.PreguntaViewSet) #URL de preguntas

urlpatterns = [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   path('api/v1/', include(router.urls)),
   path('admin/', admin.site.urls),
   path('examen/', include(router.urls)), #URL de examen
]