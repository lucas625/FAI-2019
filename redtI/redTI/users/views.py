from django.views import generic
from .models import User
from django.contrib.auth import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
class ProfileView(generic.DetailView):
    template_name = "users/profile.html"
    model = User

class LogoutView(views.LogoutView):
    next_page = 'core:home'#redireciona ao conseguir deslogar

class LoginView(views.LoginView):
    template_name = 'users/login.html'
    next_page = 'users:profile'
    redirect_authenticated_user = True #unido ao def get, impede que o usuario crie contas estando logado

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('core:home'))
        return super(LoginView, self).get(request)
