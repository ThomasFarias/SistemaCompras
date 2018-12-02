from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import  *
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView
)
User = get_user_model()
# Create your views here.

class RegistrarUsuario(CreateAPIView):        
    serializer_class=UsuarioSerializer

    
    

class ObtenerUsuarios(APIView):
    def get(self,request):
        usuarios=User.objects.all()
        serializer=UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)