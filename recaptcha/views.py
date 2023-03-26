from json import JSONDecodeError
from typing import Final
import json

from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from core.settings_ import settings
from recaptcha import serializers


class VerifyCaptcha(APIView):
    """Calls Google endpoint to verify front-end TOKEN
    and returns information whether user is a human."""

    def __init__(self):
        super().__init__()
        self.GOOGLE_URL: Final = 'https://www.google.com/recaptcha/api/siteverify'
        self.COEFFICIENT_OF_DEFINITION_OF_PERSON: Final = 0.5
        self.HEADERS: Final = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    # This is POST endpoint that we were calling with axios in the first front-end example.
    # @extend_schema(
    #     request=serializers.ReCaptcha,
    #     methods=['POST']
    # )
    @swagger_auto_schema(
        request_body=serializers.ReCaptcha
    )
    def post(self, request, *args, **kwargs):
        # Decoding the payload
        try:
            request = json.loads(request.body.decode('utf-8'))
        except JSONDecodeError:
            return Response(
                data={'detail': 'No json in body'},
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json')

        # Taking out the token from the payload
        try:
            token_generated_on_front_end_action = request['g_recaptcha_response']
        except KeyError:
            return Response(
                data={'detail': 'No field g_recaptcha_response in json'},
                status=status.HTTP_400_BAD_REQUEST,
                content_type='application/json')

        # Creating body to send to Google for verification. You could also pass user's IP as an optional parameter but I never do that.
        body = {
            'secret': settings.DRF_RECAPTCHA_SECRET_KEY.get_secret_value(),
            'response': token_generated_on_front_end_action
        }

        # Sending the request
        google_request = requests.post(self.GOOGLE_URL,
                                       data=body,
                                       headers=self.HEADERS)
        # Receiving the response
        google_response = google_request.json()

        if google_response['success'] and \
                google_response['score'] > self.COEFFICIENT_OF_DEFINITION_OF_PERSON:

            response = {
                'success': True,
                'score': True,
            }
            status_code = status.HTTP_200_OK
        else:
            response = google_response
            status_code = google_request.status_code

        return Response(
            data=response,
            status=status_code,
            content_type='application/json')
