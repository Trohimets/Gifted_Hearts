# Generated by Django 3.2.16 on 2023-02-24 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0003_feedbacksuggestion_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsforvolunteering',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='feedbacksuggestion',
            name='message',
            field=models.TextField(max_length=512, verbose_name='Сообщение/Предложение'),
        ),
    ]