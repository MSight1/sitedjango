# Generated by Django 4.2.7 on 2023-11-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostinitsa', '0008_alter_room_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='status',
            field=models.IntegerField(choices=[(0, 'Занят'), (1, 'Свободен')], default=1),
        ),
    ]
