from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedModelSerializer)

from friends.models import FriendsModel

__all__ = (
    'FriendsSerializer',
)


class FriendsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = FriendsModel
        fields = (
            'id',
            'photo',
            'first_name',
            'last_name',
            'role_in_the_project',
        )