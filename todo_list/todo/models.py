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
    id_projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)