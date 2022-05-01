from rest_framework import serializers
from produtos import models

class ProdutosSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Produtos
        fields = '__all__'