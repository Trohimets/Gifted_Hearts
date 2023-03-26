from rest_framework.viewsets import ReadOnlyModelViewSet

from projects.models import Project
from projects.serializers import ProjectSerializer
from projects.paginations import ProjectPagination

    
class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectPagination