# Generated by Django 4.1 on 2022-08-16 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_room_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='text',
            field=models.TextField(blank=True),
        ),
    ]
