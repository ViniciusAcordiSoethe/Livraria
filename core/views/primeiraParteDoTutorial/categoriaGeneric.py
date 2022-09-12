from core.models import Categoria
from core.serializers import CategoriaSerializer

from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView


class CategoriasListCreateGeneric(ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaRetrieveUpdateDestroyGeneric(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
