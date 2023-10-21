from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages
from .models import Pergunta
from .models import Resposta
from .models import Categoria
from .models import Usuario
import random
import json


def paginaPrincipal(request):
    return render(request, "paginaPrincipal.html")


def paginaPerfil(request):
    return render(request, "paginaPerfil.html")

def Login(request):
  return render(request, "paginaLogin.html")

def Cadastro(request):
  return render(request, "paginaCadastro.html")

def paginaEscolhaConteúdo(request):
    return render(request, "paginaEscolhaConteúdo.html")


def perguntasAleatorias(request, categoria_id):
    if request.method == "POST":
        jsonPerguntas = request.POST["todasPerguntas"]
        indiceAtual = int(request.POST["indiceAtual"])
        listPerguntas = json.loads(jsonPerguntas)
        resposta_selecionada = request.POST["resposta"]
    
        pergunta_atual = listPerguntas[indiceAtual]
        resposta_correta=Resposta.objects.get(pergunta=pergunta_atual['pk'], certa=True)
        indiceAtual += 1
        respostas = Resposta.objects.filter(pergunta=listPerguntas[indiceAtual]['pk'])
      
        acertos=int(request.POST["acertos"])
        print(resposta_correta.conteudo,resposta_selecionada)
       
        if resposta_correta.conteudo==resposta_selecionada:
            acertos+=1
            print(acertos)

        context = {
          "pergunta": listPerguntas[indiceAtual],
          "jsonPerguntas": jsonPerguntas,
          "indiceAtual": indiceAtual,
          "respostas": respostas,
          "acertos": acertos
        }
        if indiceAtual >=9:
          context=gerarFrases(acertos)
          return render(request, 'paginaResultados.html', context=context)
        
        return render(request, 'paginaPerguntas.html', context=context)
    
    todasPerguntas = Pergunta.objects.filter(categoria=categoria_id)
    pergAleatorias = random.sample(list(todasPerguntas), 10)
    jsonPerguntas = serializers.serialize('json', pergAleatorias)
    listPerguntas = json.loads(jsonPerguntas)

    primeiraPergunta=listPerguntas[0]
    respostas = Resposta.objects.filter(pergunta=primeiraPergunta['pk'])

    context = {"pergunta": primeiraPergunta, "jsonPerguntas": jsonPerguntas, "indiceAtual": 0, "respostas": respostas, "acertos":0}
  
    return render(request, 'paginaPerguntas.html', context=context)


def gerarFrases(acertos):
  if acertos == 0:
    frase = "Que pena! Você não acertou nenhuma pergunta."
  elif acertos == 1 or acertos == 2 or acertos == 3:
    frase = "Vamos lá, você consegue melhorar na próxima vez!"
  elif acertos == 4 or acertos == 5:
    frase = "Você está no caminho certo, continue praticando!"
  elif acertos == 6 or acertos == 7:
    frase = "Parabéns! Continue se dedicando e alcançará um resultado ainda melhor!"
  elif acertos == 8 or acertos == 9:
    frase = "Ótimo desempenho! Continue assim."
  else:
    frase = " Uau! Você é demais!!!"
  context = {"frase": frase,
            "acertos": acertos}
  return context



def cadastrarPessoa(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        usuario = request.POST['usuario']
        email = request.POST['email']
        escola = request.POST['escola']
        serie = request.POST['serie']
        senha = request.POST['senha']
        
        # Cria um usuário do Django
        user = User.objects.create_user(username=usuario, email=email, password=senha)
        
        # Cria um objeto Usuario relacionado ao usuário
        usuario_obj = Usuario.objects.create(
            escola=escola,
            serie=serie,
            user=user
        )
        
        return render(request, 'paginaPerfil.html')
    
    return render(request, 'paginaCadastro.html')


def paginaLogin(request):
  if request.method == 'POST':
    email = request.POST['email']
    senha = request.POST['senha']
    user = authenticate(request, email=email, senha=senha)
    if user is not None:
      login (request, user)
      return render (request,'paginaEscolhaConteúdo') 
    else:
      mensagem = "Usuário ou senha inválidos."
      return render(request, 'paginaLogin.html', {'mensagem':mensagem})
  else:  
    return render(request, 'paginaLogin.html')


def redefinirSenha(request):
  if request.method == 'POST':
    form = PasswordResetForm(request.POST)
    if form.is_valid():
      form.save(request=request)
      messages.success(request, 'Um link para redefinir sua senha foi enviado para o email fornecido.')
      return render(request,'paginaPrincipal.html')  
    else:
        form = PasswordResetForm()
    
    return render(request, 'paginaMudarSenha.html', {'form': form})


def perfil(request):
    if request.user.is_authenticated:
        usuario = request.user
        try:
            perfilUsuario = Usuario.objects.get(user=usuario)
        except Usuario.DoesNotExist:
            perfilUsuario = None
        return render(request, 'paginaPerfil.html', {'perfilUsuario': perfilUsuario})
    else:
        return redirect('paginaLogin')


