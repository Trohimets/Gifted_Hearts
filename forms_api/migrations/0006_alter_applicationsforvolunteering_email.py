# Generated by Django 4.1.5 on 2023-03-21 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0005_remove_feedbacksuggestion_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationsforvolunteering',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта'),
        ),
    ]
