from django.conf.urls import url
from . import views
urlpatterns=[ 
    url(r'^$',views.Index),
    url(r'^registroUsuario$',views.registroUsuario),
    url(r'^login$',views.IniciarSesion),
   

]