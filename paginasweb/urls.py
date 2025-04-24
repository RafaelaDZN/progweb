from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_curiosidades, name='lista_curiosidades'),
    path('curiosidade/<int:id>/', views.detalhes_curiosidade, name='detalhes_curiosidade'),
]
