from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.mixins import ReprMixin

__all__ = (
    'HelpTranlationModel',
    'AutoPayModel',
)

type_transfer = (
    ('bank_card','По карте'),
    ('mobile_balance','С помощью телефона'),
    ('sbp','Через QR код'),
)


class HelpTranlationModel(models.Model, ReprMixin):
    first_name = models.CharField(verbose_name=_('имя'), max_length=100, null=False, blank=False)
    last_name = models.CharField(verbose_name=_('фамилия'), max_length=100, null=False, blank=False)
    phone = models.CharField(verbose_name=_('телефон'), max_length=100,null=False, blank=False)
    email = models.CharField(verbose_name=_('электронная почта'), max_length=100, null=False, blank=False)
    amount = models.IntegerField(verbose_name=_('сумма'),null=False, blank=False)
    type_transfer = models.CharField(verbose_name=_('тип перевода'), max_length=100, null=False, blank=False,\
                                     choices=type_transfer)
    one_time = models.BooleanField(verbose_name=_('разово'))
    monthly = models.BooleanField(verbose_name=_('ежемесячно'))
    comment = models.CharField(verbose_name=_('комментарий'),default='Помощь', max_length=1500, null=True,blank=True)

    class Meta:
        verbose_name = "Перевод"
        verbose_name_plural = "Переводы"


class AutoPayModel(models.Model,ReprMixin):
    uuid = models.CharField(max_length=200,primary_key=True)
    email = models.CharField(verbose_name=_('электронная почта'), max_length=100, null=False, blank=False)
    amount = models.FloatField(verbose_name=_('сумма'))
    date_now = models.DateField(verbose_name=_('дата перевода'))
    date_next_month = models.DateField(verbose_name=_('дата следующего перевода'))

    class Meta:
        verbose_name = "Автоплатеж"
        verbose_name_plural = "Автоплатежы"


