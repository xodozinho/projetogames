from django.urls import path, include
from . import views

#http://localhost:8000/clientes
#http://localhost:8000/clientes/inicio
app_name = 'games'
urlpatterns = [
    path('inicio', views.inicio, name='inicio'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('informacao', views.informacao, name='informacao'),



    path('form_cadastro', views.form_cadastro, name='form_cadastro'),
    path('visualizar/<int:user_id>', views.visualizar, name='visualizar'),
    path('deletar/<int:user_id>', views.deletar, name='deletar'),
    path('atualizar/<int:user_id>', views.atualizar, name='atualizar'),
    path('atualizar_informacoes', views.atualizar_informacoes, name='atualizar_informacoes')


]