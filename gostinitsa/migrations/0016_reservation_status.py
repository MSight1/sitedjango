# Generated by Django 4.2.7 on 2023-11-28 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostinitsa', '0015_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='status',
            field=models.IntegerField(choices=[(1, 'Рассмотренна'), (0, 'Не рассмотренна')], default=0, verbose_name='Статус'),
        ),
    ]