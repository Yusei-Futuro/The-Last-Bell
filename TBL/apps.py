from django.apps import AppConfig

class TblConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TBL'

def ready(self):
    import TBL.signals