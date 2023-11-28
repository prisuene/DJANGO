from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from projetos.models import Projeto, Aluno, Aluno_Projeto

# Create your views here.
def home(request):
    print('Home')
    num_projetos = Projeto.objects.all().count()
    num_alunos = Aluno.objects.all().count()
    template = loader.get_template("index.html")

    context = {
        'num_projetos': num_projetos,
        'num_alunos': num_alunos,
    }
    return HttpResponse(template.render(context=context))

def alunos(request):
    lista_alunos = Aluno.objects.all()
    output = "<br> ".join([a.nome_aluno for a in lista_alunos])
    return HttpResponse(output)

def projetos(request):
    #lista_projetos = Projeto.objects.order_by("-data_projetos")[:2]
    lista_projetos = Projeto.objects.all()
    output = "<br> ".join([p.nome_projeto for p in lista_projetos])
    template = loader.get_template("projetos.html")
    context = {
        'lista_projetos': lista_projetos,
    }
    return HttpResponse(template.render(context=context))
    
    print('Projetos')
    return HttpResponse('Página Projetos')



def alocacao(request):
    print('Página Alocação de alunos em projetos')
    return HttpResponse('Página Alocação')

