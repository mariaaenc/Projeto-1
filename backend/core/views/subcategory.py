from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import SubcategorySerializer
from backend.core.models import SubCategory


class SubcategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer