from django.apps import AppConfig


class PdfToolsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pdf_tools'
    
    def ready(self):
        import pdf_tools.signals