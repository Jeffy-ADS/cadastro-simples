from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto  # Associa o formulário ao modelo Produto
        fields = ['nome', 'tipo', 'descricao'] # Inclui todos os campos do modelo no formulário




