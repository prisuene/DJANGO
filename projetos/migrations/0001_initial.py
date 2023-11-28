# Generated by Django 4.2.2 on 2023-11-13 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_aluno', models.CharField(max_length=200)),
                ('turma', models.CharField(max_length=200)),
                ('ira', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_projeto', models.CharField(max_length=200)),
                ('data_projetos', models.DateField(verbose_name='Data de início do projeto')),
                ('nome_aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projetos.aluno')),
            ],
        ),
    ]
