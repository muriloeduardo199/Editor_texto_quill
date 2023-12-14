from django.http import Http404, JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from bs4 import BeautifulSoup
import json
from .models import Post
from .forms import PostForm
from django.http import JsonResponse


def home(request):
    artigos = Post.objects.all()
    ultimo_artigo = artigos.last() if artigos else None  # Obtém o último artigo se houver algum
    
    return render(request, 'post_list.html', {'artigos': artigos, 'ultimo_artigo': ultimo_artigo})

def salvar(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        artigo = Post(comentarios=dados['artigo'])
        artigo.save()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)  

def editar_comentario(request, comentario_id):
    comentario = get_object_or_404(Post, id=comentario_id)
    
    if request.method == 'POST':
        # Obtenha os dados do corpo da solicitação POST
        novo_conteudo = request.POST.get('content')

        # Atualiza o conteúdo do comentário e salva no banco de dados
        comentario.comentarios = novo_conteudo
        comentario.save()
        
        return JsonResponse({'status': 'success', 'novo_conteudo': novo_conteudo})
    
    return JsonResponse({'status': 'error'})

    

def excluir_comentario(request, comentario_id):
    comentario = get_object_or_404(Post, id=comentario_id)
    
    if request.method == 'POST':
        # Realiza a exclusão do comentário
        comentario.delete()
        
        return JsonResponse({'status': 'success', 'mensagem': 'Comentário excluído com sucesso'})
    
    return JsonResponse({'status': 'error', 'mensagem': 'Erro ao excluir o comentário'})