from django.shortcuts import render , redirect
from .models import Username
from django.http import JsonResponse, HttpResponse
from .form import Login, Register

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def login_true(request):
    return render(request, "login.html", {
        "form": Login
    })

def register(request):
    if request.method == "GET":
        # show interface
        return render(request, template_name="Register.html", context={
            "form": Register})
    else:
        Username.objects.create(name=request.POST["name"],
                                last_name=request.POST["last_name"],
                                user=request.POST["user"],
                                password=request.POST["password"]
                                )

        return redirect("regis/")