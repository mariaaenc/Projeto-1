from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import ProductSerializer
from backend.core.models import Product


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer