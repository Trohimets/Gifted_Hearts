# Generated by Django 3.2.16 on 2023-03-10 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forms_api', '0004_auto_20230224_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedbacksuggestion',
            name='photo',
        ),
    ]