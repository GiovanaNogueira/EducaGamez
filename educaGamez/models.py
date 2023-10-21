
from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
  nome = models.CharField(max_length=300)

class Pergunta(models.Model):
  conteudo = models.CharField(max_length=300, default=None)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, null=True)

class Resposta(models.Model):
  conteudo = models.CharField(max_length=300, default=None)
  certa = models.BooleanField(default=False)
  pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, null=True)

class Frase(models.Model):
  conteudo=models.CharField(max_length=300)
  n_resp_certa=models.CharField(max_length=3)

class Usuario (models.Model):
  is_active = models.BooleanField(default=True)
  escola = models.CharField(max_length=100)
  serie = models.CharField(max_length=15)
  soma = models.CharField(max_length=100)
  subtração =models.CharField(max_length=100)
  multiplicação = models.CharField(max_length=100)
  divisão =models.CharField(max_length=100)
  geral = models.CharField(max_length=100)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  