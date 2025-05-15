from django.urls import path
from views import ver_post,index,novo_post

urlpatterns = [
    path('', index, name='index'),
    path('novo/', novo_post, name='novo_post'),
    path('post/<int:id>/', ver_post, name='ver_post'),
]
