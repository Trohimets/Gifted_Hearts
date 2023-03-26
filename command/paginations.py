from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'CommandPagination',
)


class CommandPagination(LimitOffsetPagination):
    default_limit = 10
