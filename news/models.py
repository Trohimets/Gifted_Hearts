from django.db import models
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    date = models.DateTimeField(
        verbose_name=_('Дата создания'),
        help_text='Введите дату создания'
    )
    title = models.CharField(
        verbose_name=_('Заголовок'),
        max_length=200,
        help_text='Введите заголовок новости'
    )
    news_full_text = models.TextField(
        verbose_name=_('Содержание'),
        help_text='Введите текст новости'
    )
    news_video_link = models.URLField(
        verbose_name=_('Видео'),
        blank=True,
        help_text='Вставьте ссылку на видео'
    )

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name='news_images'
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        blank=True,
        upload_to='news_images/%Y/%m/%d/',
        help_text='Выберите изображение'
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.news.title