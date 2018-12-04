from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def Index(request):
	active_tab = 'tab1'
	return render(request,"index_bienvenida.html",{'active_tab':active_tab})

def logout(request):
	active_tab = 'tab1'
	django_logout(request)
	return render(request,"index_bienvenida.html",{'active_tab':active_tab})

@login_required(login_url='login')
def Tiendas(request):
	active_tab = 'tab2'
	if request.user.is_authenticated == True:
		return render(request,"agregarTienda.html",{'active_tab':active_tab})
	else:
		return render(request,"errorLogin.html",{'active_tab':active_tab})

@login_required(login_url='login')
def Comprar(request):
	active_tab = 'tab3'
	if request.user.is_authenticated == True:
		return render(request,"comprar.html",{'active_tab':active_tab})
	else:
		return render(request,"errorLogin.html",{'active_tab':active_tab})
    
def registroUsuario(request):
	active_tab = 'tab5'
	form=FormRegistroUsuario()
	return render(request,"RegistroUsuario.html",{'form':form,'active_tab':active_tab})


def IniciarSesion(request):
	active_tab = 'tab4'
	fail = False
	form=FormLogin()
	if request.method == 'POST':
		if request.user.is_authenticated == False:
			fail = True
			return render(request,'login.html',{'fail':fail,'form':form,	'active_tab':active_tab})
	return render(request,'login.html',{'fail':fail,'form':form,	'active_tab':active_tab})