# Generated by Django 4.1.5 on 2023-02-16 20:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название документа', max_length=200, verbose_name='Название')),
                ('description', models.TextField(help_text='Введите описание документа', verbose_name='Описание')),
                ('link', models.FileField(help_text='Выберите файл, допустимые расширения: png, jpg, pdf, doc, docx', max_length=254, upload_to='documents/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'pdf', 'doc', 'docx'])], verbose_name='Файл')),
                ('type', models.CharField(choices=[('statutory', 'Уставные'), ('documents', 'Документы'), ('reporting', 'Отчетность')], default='документы', help_text='Выберите тип', max_length=10, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
            },
        ),
    ]
