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
User = get_user_model()
# Create your views here.

class RegistrarUsuarioCreateAPIView(CreateAPIView):        
    serializer_class=UsuarioSerializer


    
    

class ObtenerUsuariosAPIView(APIView):
    def get(self,request):
        usuarios=User.objects.all()
        serializer=UsuarioSerializer(usuarios,many=True)
        return Response(serializer.data)

class LoginUsuarioAPIView(APIView):
    serializer_class=LoginUsuarioSerializer

    def post(self,request,*args,**kwargs):
        data=request.data
        serializer=LoginUsuarioSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data=serializer.data
            return Response(new_data,status=HTTP_200_OK)
        return Response(serializer.errors,status=HTTP_400_BAD_REQUEST)
