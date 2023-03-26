from django.db import models
from django.utils.translation import gettext_lazy as _

from event.models import EventModel

__all__ = (
    'FeedBackSuggestion',
    'ApplicationsForVolunteering',
    'RegistrationForEvents',
)


class FeedBackSuggestion(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_('Имя')
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Фамилия')
    )
    phone = models.CharField(
        max_length=12,
        verbose_name=_('Номер телефона')
    )
    email = models.EmailField(
        verbose_name=_('Электронная почта'),
        blank=True
    )
    message = models.TextField(
        verbose_name=_('Сообщение/Предложение'),
        max_length=512
    )
    check_agreement = models.BooleanField(
        verbose_name=_('Приняты условия пользовательского соглашения'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Время создания'))

    class Meta:
        verbose_name = 'Сообщение/Предложение'
        verbose_name_plural = 'Сообщения/Предложения'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone}'


class ApplicationsForVolunteering(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_('Имя')
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Фамилия')
    )
    email = models.EmailField(
        verbose_name=_('Электронная почта'),
        unique=True
    )
    check_agreement = models.BooleanField(
        verbose_name=_('Приняты условия пользовательского соглашения'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Время создания'))

    class Meta:
        verbose_name = 'Заявка на волонтера'
        verbose_name_plural = 'Заявки на волонтера'

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'


class RegistrationForEvents(models.Model):
    first_name = models.CharField(
        max_length=255,
        verbose_name=_('Имя')
    )
    last_name = models.CharField(
        max_length=255,
        verbose_name=_('Фамилия')
    )
    phone = models.CharField(
        max_length=12,
        verbose_name=_('Номер телефона')
    )
    email = models.EmailField(
        verbose_name=_('Электронная почта')
    )
    comment = models.TextField(verbose_name=_('Комментарий'))
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Время создания'))
    check_agreement = models.BooleanField(
        verbose_name=_('Приняты условия пользовательского соглашения'))
    event_id = models.ForeignKey(EventModel,
                                 on_delete=models.CASCADE,
                                 related_name='registrations')

    class Meta:
        verbose_name = 'Регистрация на мероприятие'
        verbose_name_plural = 'Регистрации на мероприятия'
        unique_together = ('phone', 'event_id')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.event_id.title}'
