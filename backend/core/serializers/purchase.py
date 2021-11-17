from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from backend.core.models import Purchase

class PurchaseSerializer(ModelSerializer):
    products = CharField(source="products.name")
    user = CharField(source="user.name")
    class Meta:
        model = Purchase
        fields = '__all__'