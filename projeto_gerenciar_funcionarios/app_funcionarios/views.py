from django.shortcuts import render
from .models import Funcionario

def home(request):
    return render(request, 'funcionarios/home.html')

def funcionarios(request):
    if request.method == 'POST':
        novo_funcionario = Funcionario(
            nome=request.POST.get('nome'),
            sobrenome=request.POST.get('sobrenome'),
            cpf=request.POST.get('cpf'),
            remuneracao=request.POST.get('remuneracao')
        )
        novo_funcionario.save()

    contexto = {
        'funcionarios': Funcionario.objects.all()
    }

    return render(request, 'funcionarios/funcionarios.html', contexto)
