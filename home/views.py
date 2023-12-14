# views.py
from django.http import Http404, JsonResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post
from bs4 import BeautifulSoup
import json
from .models import Post
from .forms import PostForm
from django.http import JsonResponse

class ComentarioView(View):
    # Define o template para renderizar a lista de artigos
    template_name = 'post_list.html'

    def get(self, request):
        # Obtém todos os artigos do banco de dados
        artigos = Post.objects.all()
        # Obtém o último artigo se houver algum
        ultimo_artigo = artigos.last() if artigos else None
        # Retorna o template com o contexto
        return render(request, self.template_name, {'artigos': artigos, 'ultimo_artigo': ultimo_artigo})

    def post(self, request, pk=None):
    # Verifica o tipo de conteúdo da requisição
        if request.content_type == 'application/json':
            # Tenta analisar o corpo da requisição como JSON
            try:
                dados = json.loads(request.read().decode('utf-8'))
                # Cria um novo artigo com o comentário recebido
                artigo = Post(comentarios=dados['artigo'])
                # Salva o artigo no banco de dados
                artigo.save()
                # Retorna uma resposta JSON de sucesso
                return JsonResponse({'status': 'success'})
            except json.JSONDecodeError as e:
                # Imprime o erro e o corpo da requisição para depuração
                print(e)
                print(request.body)
                # Retorna uma resposta JSON de erro
                return JsonResponse({'status': 'error', 'message': 'Erro no formato JSON'}, status=400)
        else:
            # Retorna uma resposta JSON de erro
            return JsonResponse({'status': 'error', 'message': 'Tipo de conteúdo inválido'}, status=400)


    def put(self, request, pk):
        # Obtém o comentário pelo id ou retorna um erro 404
        comentario = get_object_or_404(Post, id=pk)
        # Verifica o tipo de conteúdo da requisição
        if request.content_type == 'application/x-www-form-urlencoded':
            # Obtém o novo conteúdo do comentário da requisição
            token = str(request.body)
            remove__b_token = token.replace("b'content=", "") 
            remove__b_token = remove__b_token.replace("'", "") 
            novo_conteudo = remove__b_token
            # Atualiza o conteúdo do comentário e salva no banco de dados
            comentario.comentarios = novo_conteudo
            comentario.save()
            # Retorna uma resposta JSON de sucesso
            return JsonResponse({'status': 'success', 'novo_conteudo': novo_conteudo})
        else:
            # Retorna uma resposta JSON de erro
            return JsonResponse({'status': 'error', 'message': 'Tipo de conteúdo inválido'}, status=400)


    def delete(self, request, pk):
        # Obtém o comentário pelo id ou retorna um erro 404
        comentario = get_object_or_404(Post, id=pk)
        # Exclui o comentário do banco de dados
        comentario.delete()
        # Retorna uma resposta JSON de sucesso
        return JsonResponse({'status': 'success', 'mensagem': 'Comentário excluído com sucesso'})
