from rest_framework import serializers

__all__ = (
    'ReCaptcha',
)


class ReCaptcha(serializers.Serializer):
    g_recaptcha_response = serializers.CharField()
