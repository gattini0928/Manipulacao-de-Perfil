from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.views.generic import DetailView, TemplateView, UpdateView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Perfil
from .forms import PerfilForm, CriarContaForm, LoginForm
from django.shortcuts import get_object_or_404

class HomepageView(TemplateView):
    template_name = 'homepage.html'

class CriarContaView(CreateView):
    form_class = CriarContaForm
    template_name = 'criar_conta.html'
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(self.request, f'Usuário {user.username} criado com sucesso')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, f'Erro de credenciais')
        return super().form_invalid(form)
    
class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = reverse_lazy('perfil')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            messages.success(self.request, 'Login realizado com sucesso!')
            return super().form_valid(form)
        else:
            messages.error(self.request, 'Credenciais incorretas')
            return self.form_invalid(form)

class PerfilView(LoginRequiredMixin, DetailView):
    template_name = 'perfil.html'
    model = Perfil

    def get_object(self):
        return get_object_or_404(Perfil, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PerfilForm(instance=self.object)
        return context

class EditarPerfilView(LoginRequiredMixin, UpdateView):
    model = Perfil
    template_name = 'perfil.html'
    form_class = PerfilForm

    def form_valid(self, form):
        messages.success(self.request, "Perfil atualizado com sucesso!")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('perfil')

    def get_object(self):
        return self.request.user.perfil

@login_required
def fazer_logout(request):
    logout(request)
    return redirect('homepage')
