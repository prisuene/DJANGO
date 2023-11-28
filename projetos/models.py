from django.db import models

# Create your models here.

class Aluno (models.Model):
    nome_aluno=models.CharField(max_length=200)
    turma=models.CharField(max_length=200)
    ira=models.IntegerField(default=0)

class Projeto (models.Model):
    nome_projeto=models.CharField(max_length=200)
    data_projetos=models.DateField("Data de início do projeto")

class Aluno_Projeto(models.Model):
    nome_aluno=models.ForeignKey(Aluno, on_delete=models.CASCADE)
    nome_projeto=models.ForeignKey(Projeto, on_delete=models.CASCADE)



