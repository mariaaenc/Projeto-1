from rest_framework.serializers import ModelSerializer

from backend.core.models import SubCategory

class SubcategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'