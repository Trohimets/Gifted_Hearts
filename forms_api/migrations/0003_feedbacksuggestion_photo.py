# Generated by Django 3.2.16 on 2023-02-22 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0002_auto_20230222_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbacksuggestion',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='feedback_photo/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]