# Generated by Django 4.1.5 on 2023-03-21 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photoeventmodel',
            name='id_event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_images', to='event.eventmodel'),
        ),
    ]
