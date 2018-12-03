from django.shortcuts import render
from .forms import *

# Create your views here.


def Index(request):
    return render(request,"index.html")
    
def registroUsuario(request):
    form=FormRegistroUsuario()
    return render(request,"RegistroUsuario.html",{'form':form})


def IniciarSesion(request):
    return render(request,'login.html')