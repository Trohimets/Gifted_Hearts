# Generated by Django 3.2.16 on 2023-01-21 10:49

from django.db import migrations, models
import utils.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutoPayModel',
            fields=[
                ('uuid', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=100, verbose_name='электронная почта')),
                ('amount', models.FloatField(verbose_name='сумма')),
                ('date_now', models.DateField(verbose_name='дата перевода')),
                ('date_next_month', models.DateField(verbose_name='дата следующего перевода')),
            ],
            options={
                'verbose_name': 'Автоплатеж',
                'verbose_name_plural': 'Автоплатежы',
            },
            bases=(models.Model, utils.mixins.ReprMixin),
        ),
        migrations.CreateModel(
            name='HelpTranlationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия')),
                ('phone', models.CharField(max_length=100, verbose_name='телефон')),
                ('email', models.CharField(max_length=100, verbose_name='электронная почта')),
                ('amount', models.IntegerField(verbose_name='сумма')),
                ('type_transfer', models.CharField(choices=[('bank_card', 'По карте'), ('mobile_balance', 'С помощью телефона'), ('sbp', 'Через QR код')], max_length=100, verbose_name='тип перевода')),
                ('one_time', models.BooleanField(verbose_name='разово')),
                ('monthly', models.BooleanField(verbose_name='ежемесячно')),
                ('comment', models.CharField(blank=True, default='Помощь', max_length=1500, null=True, verbose_name='комментарий')),
            ],
            options={
                'verbose_name': 'Перевод',
                'verbose_name_plural': 'Переводы',
            },
            bases=(models.Model, utils.mixins.ReprMixin),
        ),
    ]
