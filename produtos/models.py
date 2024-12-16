import datetime
from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=300)
    log_date = models.DateTimeField(default=datetime.datetime.now)  # Corrige o uso de datetime.now

    def __str__(self):
        return self.nome

