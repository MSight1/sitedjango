# Generated by Django 4.2.7 on 2023-11-12 22:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gostinitsa', '0009_alter_room_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='status',
            new_name='is_status',
        ),
    ]