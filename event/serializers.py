from rest_framework.serializers import ModelSerializer

from event import models

__all__ = (
    'EventSerializer',
    'PhotoEventSerializer',
)


class PhotoEventSerializer(ModelSerializer):
    class Meta:
        model = models.PhotoEventModel
        fields = (
            'id',
            'id_event',
            'photo',
        )


class EventSerializer(ModelSerializer):
    event_images = PhotoEventSerializer(
        many=True
    )

    class Meta:
        model = models.EventModel
        fields = (
            'id',
            'title',
            'address',
            'time',
            'desc',
            'event_images'
        )
