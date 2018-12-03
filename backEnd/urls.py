from django.conf.urls import url
from . import views
urlpatterns=[ 
    url(r'^registrar$',views.RegistrarUsuarioCreateAPIView.as_view()),
    url(r'^verUsuarios$',views.ObtenerUsuariosAPIView.as_view()),
    url(r'^login$',views.LoginUsuarioAPIView.as_view()),
    

]