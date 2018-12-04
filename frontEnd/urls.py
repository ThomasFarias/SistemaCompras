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
    path('agregarLista/', views.AgregarListaView.as_view(), name='crear_lista'),  # <--
   

]