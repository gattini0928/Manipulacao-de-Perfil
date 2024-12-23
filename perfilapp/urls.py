from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('logout/', fazer_logout, name='fazer_logout'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    # path('perfil/editar/', EditarPerfilView.as_view(), name='editar_perfil'),
]
