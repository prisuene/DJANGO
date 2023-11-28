from django.contrib import admin
from django.urls import path
from projetos import views
#from django.views.generic import RedirectView

urlpatterns = [
    #path('', RedirectView.as_view(url='/blog/'),
    path('',views.home, name='home'),
    path('projetos',views.projetos, name='projetos'),
    path('alunos',views.alunos, name='alunos'),
    path('alocacao',views.alunos, name='alocacao'),
]