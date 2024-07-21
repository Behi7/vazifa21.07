from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'login-register.html'

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.views.generic import CreateView, FormView, LogoutView

from .models import User

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','password')


class LoginForm(AuthenticationForm):
    pass


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'login-register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login-register.html'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return redirect('index')


class LogoutView(LogoutView):
    pass
