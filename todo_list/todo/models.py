from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField()
    inicio = models.DateTimeField(default=datetime.now, blank=True)
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('PEN', 'pendente'),
        ('AND', 'Em andamento'),
        ('CON', 'Concluída'),
    ]

    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='PEN')
    inicio = models.DateTimeField(default=datetime.now(), blank=True)
    responsaveis = models.ManyToManyField(User, related_name='tarefas')

    def __str__(self):
        return self.nome
    

class Nota(models.Model):
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.TextField()
    publicada = models.BooleanField(default=False)
    criado_em = models.DateTimeField(default=datetime.now(), blank=True)
    atualizado_em = models.DateTimeField(default=datetime.now(), blank=True)