from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
import json
from .models import Jogo
from rest_framework.status import HTTP_200_OK


#create…….


# Create your views here.

def inicio(request):

    return render(request, 'inicio.html')

def form_cadastro(request):
    return render(request, 'cadastro.html')

def informacao(request):
    games = Jogo.objects.all()
    contexto = {
        'games': games
    }
    return render(request, 'informacao.html',contexto)

def visualizar(request, user_id):
        if request.method == 'GET':
            jogo = Jogo.objects.filter(id=user_id)
            contexto = {
                'jogo': jogo
            }
        return render(request, 'visualizar.html', contexto)


def atualizar(request, user_id):
    if request.method == 'GET':
        jogo = Jogo.objects.filter(id=user_id)
        contexto = {
            'dados_jogo': jogo
        }
    return render(request, 'atualizar.html', contexto)


@csrf_exempt

def deletar(request, user_id):
    if request.method == 'GET':
        jogo = Jogo.objects.filter(id=user_id)
        jogo.delete()
    return HttpResponseRedirect('/games/informacao')

def cadastro(request):
    response = {}

    if request.method == 'POST':
        jogo = Jogo()
        jogo.nome = request.POST.get('nome')
        jogo.genero = request.POST.get('genero')
        jogo.email = request.POST.get('email')
        jogo.plataforma = request.POST.get('plataforma')
        jogo.save()

        response = {
            'response': HTTP_200_OK
        }
    return HttpResponse(json.dumps(response))


def atualizar_informacoes(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        genero = request.POST.get('genero')
        email = request.POST.get('email')
        plataforma = request.POST.get('plataforma')
        user_id = request.POST.get('user_id')


        jogo = Jogo.objects.filter(id=user_id)
        jogo.update(nome=nome, genero=genero, email=email, plataforma=plataforma)

        return HttpResponseRedirect('/games/informacao')











