from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class HelpTranslationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'help_translation'
    verbose_name = _('Управление разделом помочь переводом')