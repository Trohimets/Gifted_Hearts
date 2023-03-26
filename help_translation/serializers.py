from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedModelSerializer)

from help_translation.models import HelpTranlationModel, AutoPayModel

__all__ = (
    'HelpTranlationSerializer',
    'AutoPaySerializer',
)





class HelpTranlationSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = HelpTranlationModel
        fields = (
        'id',
        'first_name',
        'last_name',
        'phone',
        'email',
        'amount',
        'type_transfer',
        'one_time',
        'monthly',
        'comment'
        )

class AutoPaySerializer(HyperlinkedModelSerializer):
    class Meta:
        model = AutoPayModel
        fields = (
            'uuid'
        )

