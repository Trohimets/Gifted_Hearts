from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedModelSerializer)

from company import models

__all__ = (
    'CompanySerializer',
)


class CompanySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.CompanyModel
        fields = (
            'id',
            'logo',
            'title',
            'desc',
        )
