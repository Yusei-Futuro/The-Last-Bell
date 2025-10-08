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
from TBL.views import sing, dialogue_view, choice_view, main

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", sing),
    path("main/", main),


    #Parte del game
    path('', dialogue_view, {'dialogue_id': 1}, name='home'),
    path('dialogue/<int:dialogue_id>/', dialogue_view, name='dialogue_view'),
    path('choice/<int:choice_id>/', choice_view, name='choice_view'),
]
