from django.shortcuts import render , redirect, get_object_or_404
from .models import Username, Dialogue, Choice
from django.http import JsonResponse, HttpResponse
from .form import Login, Register

# Create your views here.

def hello(request):
    return HttpResponse("Hello world")

def login_true(request):
        if request.method == "GET":
            return render(request, "login.html", {
                "form": Login
            })
        else:
            form = Login(request.POST)
            if form.is_valid():
                username = form.cleaned_data["user"]
                password = form.cleaned_data["password"]

                user=Username.objects.filter(user=username, password=password).first()
                if user:
                    return redirect("Main/")
                else:
                    form.add_error(None, "Usuario o contraseña incorrectos")

            return render(request, "login.html", {
                "form": form
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

#Parte de pablo sobre el game

def dialogue_view(request, dialogue_id):
    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)
    choices = Choice.objects.filter(dialogue=dialogue) if dialogue.decision_point else []
    return render(request, 'game/dialogue.html', {'dialogue': dialogue, 'choices': choices})

def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'game/consequence.html', {'choice': choice})