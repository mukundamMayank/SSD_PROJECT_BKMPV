# Generated by Django 2.2.12 on 2021-11-24 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20211124_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='added_on',
            field=models.TimeField(default=datetime.datetime(2021, 11, 24, 18, 6, 54, 310273)),
        ),
        migrations.AddField(
            model_name='tasks',
            name='updated_on',
            field=models.TimeField(default=datetime.datetime(2021, 11, 24, 18, 6, 54, 310294)),
        ),
    ]
