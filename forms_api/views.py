from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from forms_api import models
from forms_api import serializers

__all__ = (
    'FeedBackSuggestion',
    'ApplicationsForVolunteering',
    'RegistrationForEvents',
)


class CreateCustomModelMixin(CreateModelMixin):
    def create(self, request, *args, **kwargs):
        try:
            check_agreement = request.data['check_agreement']
        except KeyError:
            return Response('check_agreement must have',
                            status.HTTP_400_BAD_REQUEST)
        if not check_agreement:
            return Response(
                'Without accepting the agreement, it is impossible to create',
                status.HTTP_400_BAD_REQUEST)

        try:
            response = super().create(request, *args, **kwargs)
        except (ValidationError, IntegrityError):
            return Response('Already exists or incorrect data.',
                            status.HTTP_208_ALREADY_REPORTED)
        return response


class FeedBackSuggestion(CreateCustomModelMixin, GenericViewSet):
    queryset = models.FeedBackSuggestion.objects.all()
    serializer_class = serializers.FeedBackSuggestion


class ApplicationsForVolunteering(CreateCustomModelMixin, GenericViewSet):
    queryset = models.ApplicationsForVolunteering.objects.all()
    serializer_class = serializers.ApplicationsForVolunteering


class RegistrationForEvents(CreateCustomModelMixin, GenericViewSet):
    queryset = models.RegistrationForEvents.objects.all()
    serializer_class = serializers.RegistrationForEvents
