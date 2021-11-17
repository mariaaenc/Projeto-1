from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from backend.core.models import Product

class ProductSerializer(ModelSerializer):
    category = CharField(source="category.description")
    class Meta:
        model = Product
        fields = '__all__'