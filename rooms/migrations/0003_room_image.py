# Generated by Django 4.1 on 2022-08-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_rename_rooms_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='image',
            field=models.URLField(blank=True),
        ),
    ]