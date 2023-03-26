from django.db import models
from django.utils.translation import gettext_lazy as _


class Project(models.Model):
    title = models.CharField(
        verbose_name=_('Название'),
        max_length=200,
        help_text='Введите название проекта'
    )
    desc = models.TextField(
        verbose_name=_('Описание'),
        help_text='Введите описание проекта'
    )

    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='project_images'
    )
    image = models.ImageField(
        verbose_name=_('Изображение'),
        blank=True,
        upload_to='project_images/%Y/%m/%d/',
        help_text='Выберите изображение'
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

    def __str__(self):
        return self.project.title
