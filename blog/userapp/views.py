from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'

# Create your views here.
