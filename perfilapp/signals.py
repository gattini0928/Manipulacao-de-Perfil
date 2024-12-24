from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Perfil

@receiver(post_save, sender=User)
def criar_perfil(sender, instance, created, **kwargs):
    if created and not hasattr(instance, 'perfil'):
        Perfil.objects.create(user=instance, 
                              bio='Você ainda não possui uma bio', 
                              status='Digite um status')

@receiver(post_save, sender=User)
def salvar_perfil(sender, instance, **kwargs):
    instance.perfil.save()
