# Generated by Django 2.2.12 on 2021-11-28 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20211127_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordings',
            name='notes',
            field=models.TextField(null=True),
        ),
        migrations.DeleteModel(
            name='Notes',
        ),
    ]
