# Generated by Django 2.2.12 on 2021-11-27 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20211125_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='connections',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='participants',
            name='added_on',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='recordings',
            name='created_on',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='added_on',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated_on',
            field=models.TimeField(null=True),
        ),
    ]
