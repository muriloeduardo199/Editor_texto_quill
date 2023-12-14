# urls.py
from django.urls import path
from .views import ComentarioView

urlpatterns = [
    path('', ComentarioView.as_view(), name='home'),
    path('salvar/', ComentarioView.as_view(), name='salvar'),
    path('editar-comentario/<int:pk>/', ComentarioView.as_view(), name='editar_comentario'),
    path('excluir-comentario/<int:pk>/', ComentarioView.as_view(), name='excluir_comentario'),
]
