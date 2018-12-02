from django.conf.urls import url
from . import views
urlpatterns=[ 
    url(r'^registrar$',views.RegistrarUsuario.as_view()),
    url(r'^verUsuarios$',views.ObtenerUsuarios.as_view())

]