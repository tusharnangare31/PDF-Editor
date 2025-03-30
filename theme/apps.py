from django.apps import AppConfig
from tailwind.apps import TailwindConfig

class ThemeConfig(TailwindConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'theme' 