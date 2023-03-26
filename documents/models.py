from django.db import models
from django.core.validators import FileExtensionValidator

class Document(models.Model):
    STATUTORY = 'statutory'
    DOCS = 'documents'
    REPORT = 'reporting'
    TYPE_CHOICES = [
        (STATUTORY, 'Уставные'),
        (DOCS, 'Документы'),
        (REPORT, 'Отчетность'),
    ]
    title = models.CharField(
        verbose_name='Название',
        max_length=200,
        help_text='Введите название документа'
    )
    description = models.TextField(
        verbose_name='Описание',
        help_text='Введите описание документа'
    )
    link = models.FileField(
        max_length=254,
        upload_to='documents/%Y/%m/%d/',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'pdf', 'doc', 'docx'])],
        help_text='Выберите файл, допустимые расширения: png, jpg, pdf, doc, docx',
        verbose_name='Файл'
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default='документы',
        verbose_name='Тип',
        help_text='Выберите тип'
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"

    def __str__(self):
        return self.title