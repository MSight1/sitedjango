# Generated by Django 4.2.7 on 2023-12-11 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gostinitsa', '0004_alter_gostinitsa_options_alter_room_room_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='room',
            unique_together={('room_number', 'hotel')},
        ),
    ]
