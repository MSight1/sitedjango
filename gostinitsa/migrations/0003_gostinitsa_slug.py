# Generated by Django 4.2.7 on 2023-11-09 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gostinitsa', '0002_remove_gostinitsa_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='gostinitsa',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=255),
        ),
    ]