from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'CompanyPagination',
)


class CompanyPagination(LimitOffsetPagination):
    default_limit = 10
