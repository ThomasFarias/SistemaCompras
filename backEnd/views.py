from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import  *
from rest_framework.parsers import JSONParser
from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView

)
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
Cliente = get_user_model()
# Create your views here.

class RegistrarUsuarioCreateAPIView(CreateAPIView):        
    serializer_class=UsuarioSerializer


    
    

class ObtenerUsuariosAPIView(APIView):
    def get(self,request):
        usuarios=Cliente.objects.all()
        serializer=UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)

