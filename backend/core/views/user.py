from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import UserSerializer
from backend.core.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer