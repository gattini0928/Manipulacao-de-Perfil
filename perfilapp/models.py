from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='perfil')
    bio = models.TextField(max_length=250, blank=True)
    status = models.TextField(max_length=100, blank=True)
    data_criacao = models.DateField(auto_now_add=True)
    foto_perfil = models.ImageField(default='perfil/defaultperfil.png', blank=True)

    def __str__(self):
        return self.user.username

