from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='post_list'),
    path('create', views.salvar, name='post_create'),
    path('editar-comentario/<int:comentario_id>/', views.editar_comentario, name='editar_comentario'),
    path('excluir-comentario/<int:comentario_id>/', views.excluir_comentario, name='excluir_comentario'),
]
