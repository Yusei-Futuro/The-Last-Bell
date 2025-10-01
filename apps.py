from django.apps import AppConfig

class TLBConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TLB'

    def ready(self):
        import TLB  # ✅ Aquí sí puedes importar cosas, pero con contexto