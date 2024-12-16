from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produtos/', views.listar_produtos, name='listar_produtos'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]
