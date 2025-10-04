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
from TBL.views import login_true, register, hello,  dialogue_view, choice_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_true),
    path("regis/", register),
    path("menu/", hello),

    #URL de las situaciones

    path("menu/", hello),
    path("menu/", hello),
    path("menu/", hello),
    path("menu/", hello),
    path("menu/", hello),

    path('', views.dialogue_view, {'dialogue_id': 1}, name='home'),
    path('dialogue/<int:dialogue_id>/', views.dialogue_view, name='dialogue_view'),
    path('choice/<int:choice_id>/', views.choice_view, name='choice_view'),
]
