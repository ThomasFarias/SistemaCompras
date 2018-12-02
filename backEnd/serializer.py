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

User = get_user_model()

class UsuarioSerializer(ModelSerializer):
    username=CharField(label='Usuario')
    password=CharField(label='Contraseña')
    password2 =CharField(label='Confirmar contraseña')
    email=EmailField(label='Correo Electronico')
    class Meta:
        model = User

        fields=[
            'username',
            'password',
            'password2',
            'email',            
        ]
        
        extra_kwargs={"password":
                        {"write_only":True}
                        }
    def validate(self,data):
        email=data['email']
        user=User.objects.filter(email=email)
        if user.exists():
            raise ValidationError("Este correo ya esta vinculado a un usuario.")
        return    
    def validate_password2(self,value):
        data=self.get_initial()
        password1=data.get("password")
        password2=value
        if password1 != password2:
            raise ValidationError("Las contraseñas debe coincidir")
            return value
        
    def create(self, validated_data):
        username=validated_data['username']
        email=validated_data['email']
        password=validated_data['password']
        user_obj = User(
            username=username,
            email=email
        )
        user_obj.set_password(password)
        user_obj.save()

        return validated_data

class LoginUsuarioSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username=CharField(label='Usuario')
    password=CharField(label='Contraseña')
    class Meta:
        model = User

        fields=[
            'username',
            'password',
            'token'          
        ]
        
        extra_kwargs={"password":
                        {"write_only":True}
                        }
    def validate(self,data):
        user_obj=None
        username=data["username"]
        password=data["password"]

        user = User.objects.filter(
            Q(username=username)).distinct()
        if user.exists() and user.count() ==1:
            user_obj=user.first()
        else:
            raise ValidationError("El usuario no existe.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Contraseña incorrecta")
        data["token"]="TOKEN"
        return data