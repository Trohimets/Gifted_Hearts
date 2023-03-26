from rest_framework.serializers import ModelSerializer

from projects.models import Project, ProjectImage

__all__ = (
    'ProjectSerializer',
    'ProjectImageSerializer'
)


class ProjectImageModelSerializer(ModelSerializer):
    class Meta:
        model = ProjectImage
        fields = ['image', 'project']


class ProjectSerializer(ModelSerializer):
    project_images = ProjectImageModelSerializer(
        many=True
    )

    class Meta:
        model = Project
        fields = ['id', 'title', 'desc', 'project_images']
