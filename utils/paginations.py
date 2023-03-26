from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'BasePagination',
)


class BasePagination(LimitOffsetPagination):
    default_limit = 20
