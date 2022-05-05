from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from produtos.api.serializers import ProdutosSerializer
from rest_framework import viewsets, permissions
from .models import Produtos


class ProdutoList(viewsets.ModelViewSet):
  queryset = Produtos.objects.all()
  serializer_class = ProdutosSerializer
  permission_classes = [permissions.IsAuthenticated]
  filter_backends = [DjangoFilterBackend, SearchFilter]
  filterset_fields = ['categoria']
  search_fields = ['title', 'description',]