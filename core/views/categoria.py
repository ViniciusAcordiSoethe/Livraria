from core.models import Categoria
from rest_framework.permissions import IsAuthenticated
from core.serializers import CategoriaSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.

class CategoriaViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer