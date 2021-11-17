from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import PurchaseSerializer
from backend.core.models import Purchase


class PurchaseViewSet(ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer