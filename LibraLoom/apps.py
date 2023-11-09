from django.apps import AppConfig


class LibraLoomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LibraLoom'

# apps.py
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'LibraLoom'

    def ready(self):
        import LibraLoom.signals  # Import your signals module
