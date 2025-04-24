from django.shortcuts import render, get_object_or_404, redirect
from .models import Curiosidade, Comentario, Categoria
from django.contrib.auth.decorators import login_required

# Listar curiosidades
def lista_curiosidades(request):
    curiosidades = Curiosidade.objects.all().order_by('-data_criacao')  # Ordena do mais recente
    return render(request, 'forum/lista_curiosidades.html', {'curiosidades': curiosidades})

# Detalhes de uma curiosidade
def detalhes_curiosidade(request, id):
    curiosidade = get_object_or_404(Curiosidade, pk=id)
    if request.method == "POST":
        comentario_texto = request.POST.get('comentario')
        if comentario_texto:
            comentario = Comentario(post=curiosidade, autor=request.user, texto=comentario_texto)
            comentario.save()
            return redirect('detalhes_curiosidade', id=id)
    return render(request, 'forum/detalhes_curiosidade.html', {'curiosidade': curiosidade})

# Adicionar nova curiosidade (apenas usuários logados)
@login_required
def adicionar_curiosidade(request):
    if request.method == "POST":
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        categoria_id = request.POST.get('categoria', None)
        categoria = Categoria.objects.get(id=categoria_id) if categoria_id else