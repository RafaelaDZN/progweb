from django.shortcuts import render, redirect, get_object_or_404
from models import Post
from forms import PostForm 


def index(request):
    posts = Post.objects.all().order_by('-criado_em')
    return render(request, 'paginasweb/index.html', {'posts': posts})


def novo_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'paginasweb/form.html', {'form': form})


def ver_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'paginasweb/sobre.html', {'post': post})
