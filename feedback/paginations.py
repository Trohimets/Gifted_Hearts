from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'FeedbackPagination',
)


class FeedbackPagination(LimitOffsetPagination):
    default_limit = 10
