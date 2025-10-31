"""
URL configuration for Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from TBL.views import sign, main, main_game, logo_out, singin, main_game, new_game, prologue, load_game, play_situations, make_choice, situation_complete, continue_to_next_day,game_complete

urlpatterns = [
    path('admin/', admin.site.urls),
    path("singup/", sign, name="sing"),
    path("", main, name="main_player"),
    path("logout/", logo_out, name="logout"),
    path("singin/", singin, name="singin"),
    path('game/', main_game, name='main_game'),
    path('game/new/', new_game, name='new_game'),
    path('game/prologue/', prologue, name='prologue'),
    path('game/load/', load_game, name='load_game'),
    path('game/situation/<int:situation_id>/', play_situations, name='play_situation'),
    path('game/choice/<int:choice_id>/', make_choice, name='make_choice'),
    path('game/situation/<int:situation_id>/complete/', situation_complete, name='situation_complete'),
    path('game/next-day/', continue_to_next_day, name='continue_to_next_day'),
    path('game/complete/', game_complete, name='game_complete'),
]
