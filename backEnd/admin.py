from django.contrib import admin
from .models import  Tienda, Lista, Producto

# Register your models here.
admin.site.register(Tienda)
admin.site.register(Lista)
admin.site.register(Producto)