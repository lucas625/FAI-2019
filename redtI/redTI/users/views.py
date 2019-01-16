from django.views import generic
from .models import User
from django.contrib.auth import views, get_user_model, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import auth
from .forms import UserForm
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

class CadastroView(views.FormView):
    form_class = UserForm
    template_name = "users/cadastro.html"#bom para modelos personalizados de cadastro
    model = get_user_model()
    redirect_authenticated_user = True #unido ao def get, impede que o usuario crie contas estando logado

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('core:home'))
        return super(CadastroView, self).get(request)

    def form_valid(self, form):
        self.object = form.save()
        user = authenticate(username=self.object.email, password=form.cleaned_data['password'])
        auth.login(self.request, user)#faz o login automatico

        return redirect('core:home')