from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'NewsPagination',
)


class NewsPagination(LimitOffsetPagination):
    default_limit = 10
