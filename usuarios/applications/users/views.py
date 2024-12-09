from django.shortcuts import render
from django.views.generic import (
    CreateView
)
# Create your views here.


class UserRegisterView(CreateView):
    template_name="users/register.html"