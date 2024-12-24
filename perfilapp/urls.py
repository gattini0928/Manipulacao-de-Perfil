from django.urls import path
from .views import *

urlpatterns = [
    path('', HomepageView.as_view(), name="homepage"),
    path('logout/', fazer_logout, name='fazer_logout'),
    path('login/', LoginView.as_view(), name='fazer_login'),
    path('criarconta/', CriarContaView.as_view(), name='criar_conta'),
    path('perfil/', PerfilView.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfilView.as_view(), name='editar_perfil'),
]
