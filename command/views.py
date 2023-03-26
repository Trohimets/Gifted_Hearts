from rest_framework.viewsets import ReadOnlyModelViewSet

from command.models import Command
from command.serializers import CommandSerializer
from command.paginations import CommandPagination

__all__ = (
    'CommandViewSet',
)


class CommandViewSet(ReadOnlyModelViewSet):
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    pagination_class = CommandPagination
