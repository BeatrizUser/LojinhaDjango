from django.contrib import admin

# Register your models here.
from .models import Produtos

# Abaixo jeito mais simples de importar a lista para o admin.
admin.site.register(Produtos)
