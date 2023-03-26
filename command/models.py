from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.mixins import ReprMixin

__all__ = (
    'Command',
)


class Command(models.Model, ReprMixin):
    photo = models.ImageField(verbose_name=_('Фотография'),
                             upload_to='photo/',
                             blank=True,
                             null=True)
    first_name = models.CharField(verbose_name=_('Имя'), max_length=100, null=True)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=100, null=True)
    role_in_the_project = models.TextField(verbose_name=_('Роль в проекте'), null=True)

    class Meta:
        verbose_name = "Член команды"
        verbose_name_plural = "Члены команды"