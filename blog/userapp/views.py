from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from .forms import RegistrationForm
from django.views.generic import CreateView, DeleteView
from .models import BlogUser
from django.urls import reverse_lazy, reverse
from rest_framework.authtoken.models import Token


class UserLoginView(LoginView):
    template_name = 'userapp/login.html'


class UserCreateView(CreateView):
    model = BlogUser
    template_name = 'userapp/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('userapp:login')


class UserDetailView(DeleteView):
    template_name = 'userapp/profile.html'
    model = BlogUser


def update_token(request):
    user = request.user
    if user.auth_token:
        user.auth_token.delete()
        Token.objects.create(user=user)
    else:
        token = Token.objects.create(user=request)
    return HttpResponseRedirect(reverse('userapp:profile', kwargs={'pk': user.pk}))
# Create your views here.
