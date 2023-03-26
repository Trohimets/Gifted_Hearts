from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedModelSerializer)

from command.models import Command

__all__ = (
    'CommandSerializer',
)


class CommandSerializer(ModelSerializer):
    class Meta:
        model = Command
        fields = (
            'id',
            'photo',
            'first_name',
            'last_name',
            'role_in_the_project',
        )