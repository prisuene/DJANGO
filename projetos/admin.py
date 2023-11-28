from django.contrib import admin
from .models import Aluno, Projeto,Aluno_Projeto

# Register your models here.
admin.site.register(Aluno)
admin.site.register(Projeto)
admin.site.register(Aluno_Projeto)