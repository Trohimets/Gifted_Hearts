from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class FormsApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'forms_api'
    verbose_name = _('Управление разделом отправленных форм')
