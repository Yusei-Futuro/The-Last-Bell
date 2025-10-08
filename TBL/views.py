from django.shortcuts import render , redirect, get_object_or_404
from .models import Username, Dialogue, Choice
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout

# Create your views here.
def main(request):
    return render(request,"main game.html", {
        "form": main
    })

def main_game(request):
    return render(request, "main_base.html",{
        "from": main
    })

def sing(request):
    if request.method == "GET":
        return render(request, "Login.html", {
            "form": UserCreationForm()
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"],
                                                password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("main_player")
            except:
                return render(request, "Login.html",{
                    "form": UserCreationForm(),
                    "Error": "User already exist"
                })

        return render(request,"Login.html",{
            "Form":UserCreationForm(),
            "Error": "Password not same"
        })

def logo_out(request):
    logout(request)
    return redirect("main_player")



#Parte de pablo sobre el game

def dialogue_view(request, dialogue_id):
    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)
    choices = Choice.objects.filter(dialogue=dialogue) if dialogue.decision_point else []
    return render(request, 'game/dialogue.html', {'dialogue': dialogue, 'choices': choices})

def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'game/consequence.html', {'choice': choice})