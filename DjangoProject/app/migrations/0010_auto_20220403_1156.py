# Generated by Django 2.2.27 on 2022-04-03 08:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20220403_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 3, 11, 56, 37, 33293), verbose_name='Опубликовано'),
        ),
    ]
