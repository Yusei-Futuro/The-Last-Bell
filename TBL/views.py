from django.shortcuts import render
from . import models
from django.http import JsonResponse, HttpResponse
from .form import Login, Register

# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")

def login_true(request):
    return render(request, "login.html", {
        "form": Login
    })

def register(request):
    return render(request, template_name= "Register.html", context={
        "form": Register
    })