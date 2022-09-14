from core.models import Compra
from core.serializers import CompraSerializer

from rest_framework.viewsets import ModelViewSet

class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer