from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.views.generic import DetailView, TemplateView, UpdateView, FormView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


class HomepageView(TemplateView):
    template_name = 'homepage.html'

class PerfilView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'perfil.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user
    

@login_required
def fazer_logout(request):
    logout(request)
    return render(request,'homepage.html')