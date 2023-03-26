from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.mixins import ReprMixin

__all__ = (
    'EventModel',
    'PhotoEventModel',
)


class EventModel(models.Model):
    title = models.TextField(verbose_name=_('Наименование'))
    address = models.TextField(verbose_name=_('Адрес проведения'))
    time = models.DateTimeField(verbose_name=_('Время проведения'))
    desc = models.TextField(verbose_name=_('Описание'))

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return f'{self.title}'


class PhotoEventModel(models.Model):
    id_event = models.ForeignKey(EventModel, on_delete=models.CASCADE, related_name='event_images')
    photo = models.ImageField(verbose_name=_('фото с мероприятия'),
                              upload_to='media/event/%Y/%m/%d/',
                              help_text='Выберите изображение'
                              )

    class Meta:
        verbose_name = "Фотография с мероприятия"
        verbose_name_plural = "Фотографии с мероприятия"
