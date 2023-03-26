from rest_framework.viewsets import ReadOnlyModelViewSet

from company import models
from company import serializers
from company import paginations

__all__ = (
    'CompanyView',
)


class CompanyView(ReadOnlyModelViewSet):
    queryset = models.CompanyModel.objects.all()
    serializer_class = serializers.CompanySerializer
    pagination_class = paginations.CompanyPagination
