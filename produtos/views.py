from django.shortcuts import render, redirect,get_object_or_404
from .models import Produto
from .forms import ProdutoForm  # Crie um form para o produto
from django.contrib import messages

def index(request):
    if request.method == "POST":
        form = ProdutoForm(request.POST)  # Preenche o formulário com os dados enviados
        if form.is_valid():  # Valida os dados
            form.save()  # Salva os dados no banco
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect('index')  # Redireciona para a mesma página (ou outra, se preferir)
    else:
        form = ProdutoForm()  # Exibe um formulário vazio em requisições GET
    return render(request, 'index.html', {'form': form})


def listar_produtos(request):
    produtos = Produto.objects.all()  # Busca todos os produtos no banco
    return render(request, 'listar_produtos.html', {'produtos': produtos})



def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto atualizado com sucesso!')
            return redirect('lista_produtos')  # Redireciona para a lista de produtos
    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'editar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)

    if request.method == 'POST':
        produto.delete()
        messages.success(request, 'Produto excluído com sucesso!')
        return redirect('lista_produtos')  # Redireciona para a lista de produtos

    return render(request, 'confirmar_exclusao.html', {'produto': produto})



