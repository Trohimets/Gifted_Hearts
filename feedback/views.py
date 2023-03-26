from rest_framework.mixins import (ListModelMixin,
                                   RetrieveModelMixin,
                                   CreateModelMixin)
from rest_framework.viewsets import GenericViewSet

from feedback import models
from feedback import serializers
from feedback.paginations import FeedbackPagination

__all__ = (
    'FeedbackView',
)


class FeedbackView(ListModelMixin,
                   RetrieveModelMixin,
                   CreateModelMixin,
                   GenericViewSet):
    queryset = models.FeedbackModel.objects.all()
    serializer_class = serializers.FeedbackSerializer
    pagination_class = FeedbackPagination
