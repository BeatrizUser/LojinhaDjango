from django_filters.rest_framework import DjangoFilterBackend
from api.serializers import ProdutosSerializer
from rest_framework import viewsets, permissions
from .models import Produtos


class ProdutosViewSet(viewsets.ModelViewSet):
  queryset = Produtos.objects.all()
  serializer_class = ProdutosSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend]
  filterset_fields = ['title', 'categoria']