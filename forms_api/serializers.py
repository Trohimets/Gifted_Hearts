from rest_framework.serializers import ModelSerializer
from forms_api import models

__all__ = (
    'FeedBackSuggestion',
    'ApplicationsForVolunteering',
    'RegistrationForEvents',
)


class FeedBackSuggestion(ModelSerializer):
    class Meta:
        model = models.FeedBackSuggestion
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'message',
            'check_agreement',
        )



class ApplicationsForVolunteering(ModelSerializer):
    class Meta:
        model = models.ApplicationsForVolunteering
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'check_agreement',
        )

        def validate(self, attrs):
            try:
                models.ApplicationsForVolunteering.objects.get(email=attrs['email'])
            except models.ApplicationsForVolunteering.DoesNotExist:
                pass
            else:
                raise ApplicationsForVolunteering.ValidationError('email already exists')
            return attrs



class RegistrationForEvents(ModelSerializer):
    class Meta:
        model = models.RegistrationForEvents
        fields = (
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'comment',
            'check_agreement',
            'event_id',
        )
