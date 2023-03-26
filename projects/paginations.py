from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'ProjectPagination',
)


class ProjectPagination(LimitOffsetPagination):
  default_limit = 10

