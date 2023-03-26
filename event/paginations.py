from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'EventPagination',
)


class EventPagination(LimitOffsetPagination):
    default_limit = 10
