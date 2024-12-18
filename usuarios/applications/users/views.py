from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegisterForm, LoginForm
from .models import user
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    View,
    CreateView
)
from django.views.generic.edit import (
    FormView
)



# Create your views here.


class UserRegisterView(FormView):
    template_name = "users/register.html"
    form_class = UserRegisterForm
    success_url = "/"

    def form_valid(self, form):
        
        user.objects.create_user(
            form.cleaned_data["username"],
            form.cleaned_data["email"],
            form.cleaned_data["password1"],
            nombres=form.cleaned_data["nombres"],
            apellidos=form.cleaned_data["apellidos"],
            genero=form.cleaned_data["genero"]

        )

        return super(UserRegisterView, self).form_valid(form)
    

class LoginUser(FormView):
    template_name = "users/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("home_app:panel")

    def form_valid(self, form):
        user=authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password"],

        )
        login(self.request, user)


        return super(LoginUser, self).form_valid(form)


class LogOutView(View):
    def get(self, request, *args, **kargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                "users_app:user-login"
            )
        )

