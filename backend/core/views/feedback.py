from rest_framework.viewsets import ModelViewSet

from backend.core.serializers import FeedbackSerializer
from backend.core.models import Feedback


class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer