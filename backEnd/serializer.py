from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Tienda, EstadoTienda, Producto


from rest_framework.serializers import (
    EmailField,
    CharField,
    ModelSerializer,
    SerializerMethodField,
    ValidationError
)

Cliente = get_user_model()

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Cliente

        fields=[
            'username',
            'password',
            'email',            
        ]
        
        extra_kwargs={"password":
                        {"write_only":True}
                        }
        
    def validate(self,data):
        email=data['email']
        cliente=Cliente.objects.filter(email=email)
        if cliente.exists():
            raise ValidationError("Este correo ya esta vinculado a un usuario.")
        return  data

    def validate_password2(self,value):
        data=self.get_initial()
        password1=data.get("password")
        password2=value
        if password1 != password2:
            raise ValidationError("Las contraseñas debe coincidir")
            return value
        
    def create(self, validated_data):
        username=validated_data['username']
        print("CREANDO USUARIO")
        email=validated_data['email']
        password=validated_data['password']
        user_obj = Cliente(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data


class TiendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tienda
        fields = ('nombre_tienda',
                  'nombre_sucursal','direccion','region','ciudad',
                  'estado'
                 )

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoTienda
        fields = ('codigo_estado',
                  'estado'
                 )

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('nombre_producto',
                  'costo_presupuestado','costo_real','notas','tienda'
                 )


