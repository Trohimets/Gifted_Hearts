from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedModelSerializer)

from feedback import models

__all__ = (
    'FeedbackSerializer'
)


class FeedbackSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.FeedbackModel
        fields = (
            'id',
            'time',
            'first_name',
            'last_name',
            'body',
            'photo'
        )
