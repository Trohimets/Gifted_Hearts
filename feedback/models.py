from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.mixins import ReprMixin

__all__ = (
    'FeedbackModel',
)


class FeedbackModel(models.Model, ReprMixin):
    time = models.DateTimeField(verbose_name=_('Время создания'),
                                auto_now_add=True)
    first_name = models.CharField(verbose_name=_('Имя'), max_length=100)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=100)
    body = models.TextField(verbose_name=_('Отзыв'))
    photo = models.ImageField(verbose_name=_('Фотография'),
                             upload_to='photo/',
                             blank=True,
                             null=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
