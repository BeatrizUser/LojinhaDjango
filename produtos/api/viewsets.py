from rest_framework import viewsets
from produtos.api import serializers
from produtos import models

class ProdutosViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProdutosSerializer
    queryset = models.Produtos.objects.all()