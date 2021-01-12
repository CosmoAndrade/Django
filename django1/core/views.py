from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    

    context = {
        'curso': 'Django',
        'outro': 'Django e Massa',
        'produtos': produtos

    }

    return render(request,'index.html',context)
    

def contato(request):
    return render (request,'contato.html')