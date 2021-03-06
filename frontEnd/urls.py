from django.conf.urls import url
from django.urls import include, path
from . import views
urlpatterns=[ 
    url(r'^$',views.Index),
    url(r'^index$',views.Index,name="index"),
    url(r'^registroUsuario$',views.registroUsuario,name="registroUsuario"),
    url(r'^login$',views.IniciarSesion,name="login"),
    url(r'^logout$',views.logout,name="logout"),
    url(r'^comprar$',views.Comprar,name="comprar"),
    url(r'^agregarLista$',views.AgregarLista,name="agregarLista"),
    url(r'^agregarTiendas$',views.Tiendas,name="agregarTiendas"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^agregarProductos/(?P<codigo>\d+)/$',views.registroProducto,name="agregarProductos"),    
    url(r'^comprarProductos/(?P<codigo>\d+)/$',views.comprarProducto,name="comprarProductos"),
    url(r'^listaProductos/(?P<codigo>\d+)/$',views.ListaProductos,name="listaProductos"),
    path('agregarLista/', views.AgregarListaView.as_view(), name='crear_lista'),  # <--
    
   

]