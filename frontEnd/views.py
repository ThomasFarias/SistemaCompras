from django.shortcuts import render
from .forms import *
from django.contrib.auth import authenticate, logout as django_logout
from django.contrib.auth.decorators import login_required
from backEnd.models import Producto, Lista, Tienda
from bootstrap_modal_forms.mixins import PassRequestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.


def Index(request):
	active_tab = 'tab1'
	return render(request,"index_bienvenida.html",{'active_tab':active_tab})

def AgregarLista(request):
	if request.method == 'POST':
		form = ListaComprasForm(request.POST)
		form['codigo_usuario'] = request.user
		print(form['codigo_usuario'])

	else:
		form = ListaComprasForm()
	
	return render(request,"agregarLista.html")


class AgregarListaView(generic.CreateView):
	template_name = 'agregarLista.html'
	form_class = ListaComprasForm
	success_message = 'EXITO: Ha agregado una lista nueva.'
	success_url = reverse_lazy('comprar')

	def form_valid(self, form):
		usuario = self.request.user
		form.instance.codigo_usuario = usuario
		return super(AgregarListaView, self).form_valid(form)


def logout(request):
	active_tab = 'tab1'
	django_logout(request)
	return render(request,"index_bienvenida.html",{'active_tab':active_tab})

@login_required(login_url='login')
def Tiendas(request):
	active_tab = 'tab2'
	form=FormTienda()
	if request.user.is_authenticated == True:
		return render(request,"agregarTienda.html",{'form':form,'active_tab':active_tab})
	else:
		return render(request,"errorLogin.html",{'form':form,'active_tab':active_tab})

@login_required(login_url='login')
def Comprar(request):
	active_tab = 'tab3'
	if request.method == 'POST':
		print('POST')
		form = ListaComprasForm(request.POST)
		form['codigo_usuario'] = request.user
		print(form['codigo_usuario'])

	else:
		form = ListaComprasForm()
		print('NOPOST')
		return render(request,"comprar.html",{'usuario':request.user})

	
	return render(request,"agregarLista.html")

@login_required(login_url='login')
def registroProducto(request,codigo):
	form=FormProducto(request.POST)
	#tienda=Tenda.objects.get(codigo_lista=codigo)
	#form.instance.tienda = 
	print(form.__dict__["fields"])
	if form.is_valid():		
		print('FORMA VALIDA')
		lista=Lista.objects.get(codigo_lista=codigo)
		data=form.cleaned_data
		producto=Producto(nombre_producto=data.get("nombre_producto"),costo_presupuestado=data.get("costo_presupuestado"),costo_real=data.get("costo_real"),notas=data.get("notas"),tienda=data.get("tienda"),lista=lista)
		producto.save()	
		return render(request,'agregarProducto.html',{'form': form})	
	else:
		print('FORMA NO VALIDA')
		form.is_valid()
		form=FormProducto()
		return render(request,'agregarProducto.html',{'form': form})

@login_required(login_url="login")
def comprarProducto(request,codigo):
	producto=Producto.objects.get(codigo_prod=codigo)
	form=FormComprarProducto(request.POST)	
	if request.method=='POST':
		if form.is_valid():
							
			data=form.cleaned_data
			producto.costo_real=data.get("costo_real")
			producto.save()		
	else:
		form=FormComprarProducto(instance=producto)
		

	
	return render(request,'comprarProducto.html',{'form': form})
	

@login_required(login_url='login')
def ListaProductos(request,codigo):
	if request.method == 'POST':
		form=FormProducto(request.POST)
		if form.is_valid():		
			return render(request,'agregarProducto.html',{'form': form})
	else:
		form=FormProducto()
		print('HOLA')
		productos = Producto.objects.filter(lista=Lista.objects.get(codigo_lista=codigo))
		#productos = Producto.objects.all()
		return render(request,'listaProductos.html',{'productos': productos})
		

    
def registroUsuario(request):
	active_tab = 'tab5'
	form=FormRegistroUsuario()
	return render(request,"RegistroUsuario.html",{'form':form,'active_tab':active_tab})


def IniciarSesion(request):
	active_tab = 'tab4'
	fail = False
	form=FormLogin()
	if request.method == 'POST':
		print("ES POST")
		if request.user.is_authenticated == False:
			fail = True
			return render(request,'login.html',{'fail':fail,'form':form,	'active_tab':active_tab})
	return render(request,'login.html',{'fail':fail,'form':form,	'active_tab':active_tab})