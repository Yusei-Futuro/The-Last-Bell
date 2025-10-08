from django.shortcuts import render , redirect, get_object_or_404
from .models import Username, Dialogue, Choice
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
def main(request):
    return HttpResponse("<h1>Welcome</h1>")

def sing(request):
    if request.method == "GET":
        return render(request, "Login.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],
                                                password=request.POST["password"])
                user.save()
                login(request, user)
                return redirect("main")
            except:
                return render(request, "Login.html",{
                    "form": UserCreationForm,
                    "Error": "User already exist"
                })

        return render(request,"Login.html",{
            "Form":UserCreationForm,
            "Error": "Password not same"
        })

#Parte de pablo sobre el game

def dialogue_view(request, dialogue_id):
    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)
    choices = Choice.objects.filter(dialogue=dialogue) if dialogue.decision_point else []
    return render(request, 'game/dialogue.html', {'dialogue': dialogue, 'choices': choices})

def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'game/consequence.html', {'choice': choice})