from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import CategorySerializer
from backend.core.models import Category


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer