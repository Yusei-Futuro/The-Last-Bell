from django.contrib import admin
from django.urls import path
from TLB import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dialogue_view, {'dialogue_id': 1}, name='home'),  # Inicio del juego
    path('dialogue/<int:dialogue_id>/', views.dialogue_view, name='dialogue_view'),
    path('choice/<int:choice_id>/', views.choice_view, name='choice_view'),
]

# 🖼️ Para servir archivos multimedia en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)