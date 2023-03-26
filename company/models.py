from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.mixins import ReprMixin

__all__ = (
    'CompanyModel',
)


class CompanyModel(models.Model, ReprMixin):
    logo = models.ImageField(verbose_name=_('Логотип'),
                             upload_to='media/company_logos/%Y/%m/%d/',
                             blank=True,
                             null=True)
    title = models.TextField(verbose_name=_('Название'))
    desc = models.TextField(verbose_name=_('Чем была полезна'))

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self):
        return f'{self.title}'
