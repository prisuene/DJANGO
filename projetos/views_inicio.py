from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from projetos.models import Projeto, Aluno, Aluno_Projeto

# Create your views here.
def home(request):
    print('Home')
    return HttpResponse('Página Home')

def projetos(request):
    print('Projetos')
    return HttpResponse('Página Projetos')

def alunos(request):
    print('Página Alunos')
    return HttpResponse('Página Alunos')

def alocacao(request):
    print('Página Alocação de alunos em projetos')
    return HttpResponse('Página Alocação')