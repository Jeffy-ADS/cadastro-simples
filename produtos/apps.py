from django.apps import AppConfig

class ProdutosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'produtos'  # Deve corresponder ao nome do diretório do aplicativo
