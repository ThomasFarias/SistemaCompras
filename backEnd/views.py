from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import  *
from .models import Tienda
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

class TiendaView(APIView):
    parser_classes = (JSONParser,)
    def get(self,request):
        tiendas=Tienda.objects.all()
        serializer=TiendaSerializer(tiendas,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=TiendaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        


class ProductoView(APIView):
    parser_classes = (JSONParser,)
    def get(self,request):
        productoss=Producto.objects.all()
        serializer=ProductoSerializer(productos,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            serializer=ProductoSerializer()
            return Response(serializer.data)
    



