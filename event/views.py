from rest_framework.viewsets import ReadOnlyModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from event import models, filters
from event import serializers
from event.paginations import EventPagination

__all__ = (
    'EventView',
)


class EventView(ReadOnlyModelViewSet):
    queryset = models.EventModel.objects.all()
    serializer_class = serializers.EventSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = EventPagination
    filterset_class = filters.EventFilter
