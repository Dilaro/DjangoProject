# Generated by Django 2.2.27 on 2022-04-04 07:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20220403_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2022, 4, 4, 10, 5, 51, 976940), verbose_name='Опубликовано'),
        ),
    ]
