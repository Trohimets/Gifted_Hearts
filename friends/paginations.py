from rest_framework.pagination import LimitOffsetPagination

__all__ = (
    'FriendsPagination',
)


class FriendsPagination(LimitOffsetPagination):
    default_limit = 10
