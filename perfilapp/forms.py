from django import forms
from .models import Perfil
from django.contrib.auth.models import User

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['bio', 'status', 'foto_perfil']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'}),
            'foto_perfil': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CriarContaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'E-mail'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Senha'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 
                                                             'placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder':'Senha'}))
