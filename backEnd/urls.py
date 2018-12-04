from django.conf.urls import url
from django.urls import include, path
from . import views
urlpatterns=[ 
    url(r'^registrar$',views.RegistrarUsuarioCreateAPIView.as_view()),
    url(r'^verUsuarios$',views.ObtenerUsuariosAPIView.as_view()),
    url(r'^tienda$',views.TiendaView.as_view()),
    url(r'^estado_tienda$',views.EstadoTiendaView.as_view()),
    path('rest-auth/', include('rest_auth.urls')),
    

]