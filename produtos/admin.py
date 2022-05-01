from django.contrib import admin

from .models import Produtos

@admin.register(Produtos)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "size", "price")
    prepopulated_fields = {"slug": ("title",)}