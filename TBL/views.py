from django.shortcuts import render
from . import models
from django.http import JsonResponse, HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hola mundo")
