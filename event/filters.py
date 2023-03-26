from django_filters import rest_framework as filters
from django.db.models import QuerySet
from datetime import datetime

from event.models import EventModel

__all__ = (
    'EventFilter',
)


def get_current(query_set: QuerySet, name_param: str, flag: bool) -> QuerySet:
    if flag:
        q = query_set.filter(time__gt=datetime.now())
    else:
        q = query_set.filter(time__lt=datetime.now())
    return q


class EventFilter(filters.FilterSet):
    time = filters.DateTimeFromToRangeFilter()
    current = filters.BooleanFilter(method=get_current)

    class Meta:
        model = EventModel
        fields = (
            'time',
        )
