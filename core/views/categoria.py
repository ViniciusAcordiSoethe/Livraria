from core.models import Categoria
from core.serializers import CategoriaSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoriaViewSet(ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer