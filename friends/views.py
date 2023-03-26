from rest_framework.viewsets import ReadOnlyModelViewSet

from friends.models import FriendsModel
from friends.serializers import FriendsSerializer
from friends.paginations import FriendsPagination

__all__ = (
    'FriendsView',
)


class FriendsView(ReadOnlyModelViewSet):
    queryset = FriendsModel.objects.all()
    serializer_class = FriendsSerializer
    pagination_class = FriendsPagination
