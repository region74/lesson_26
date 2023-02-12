from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import CreateView
from .models import BlogUser
from django.urls import reverse_lazy


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('userapp:login')


# Create your views here.
