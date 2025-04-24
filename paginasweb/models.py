from django.db import models

# Categoria da curiosidade (Ex: Animais, Plantas, Fenômenos Naturais)
class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# Modelo para armazenar as curiosidades
class Curiosidade(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()  # Descrição completa da curiosidade
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relaciona com a categoria
    imagem = models.ImageField(upload_to='curiosidades/', null=True, blank=True)  # Imagem opcional
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
