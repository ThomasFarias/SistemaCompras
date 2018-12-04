from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.db.models import Q


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


class LoginUsuarioSerializer(ModelSerializer):
    username=CharField(label='Usuario')
    password=CharField(label='Contraseña')
    class Meta:
        model = Cliente

        fields=[
            'username',
            'password'       
        ]
        
        extra_kwargs={"password":
                        {"write_only":True}
                        }
    def validate(self,data):
        user_obj=None
        username=data["username"]
        password=data["password"]

        cliente = Cliente.objects.filter(
            Q(username=username)).distinct()
        if cliente.exists() and cliente.count() ==1:
            user_obj=cliente.first()
        else:
            raise ValidationError("El usuario no existe.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Contraseña incorrecta")
       
        return data