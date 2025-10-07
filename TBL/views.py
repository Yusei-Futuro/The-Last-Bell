from django.shortcuts import render , redirect, get_object_or_404
from .models import Username, Dialogue, Choice
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def main(request):
    return HttpResponse("<h1>Welcome</h1>")

def login(request):
    if request.method == "Get":
        return render(request, "Login.html", {
            "form": UserCreationForm
        })
    else:
        if request.Post["password1"] == request.Post["password2"]:
            try:
                user = User.objects.create_user(username=request.Post["username"],
                                                password=request.Post["password1"])
                user.save()
                return HttpResponse("User create")
            except:
                return HttpResponse("User save")

        return HttpResponse("Password incorrect")

#Parte de pablo sobre el game

def dialogue_view(request, dialogue_id):
    dialogue = get_object_or_404(Dialogue, pk=dialogue_id)
    choices = Choice.objects.filter(dialogue=dialogue) if dialogue.decision_point else []
    return render(request, 'game/dialogue.html', {'dialogue': dialogue, 'choices': choices})

def choice_view(request, choice_id):
    choice = get_object_or_404(Choice, pk=choice_id)
    return render(request, 'game/consequence.html', {'choice': choice})