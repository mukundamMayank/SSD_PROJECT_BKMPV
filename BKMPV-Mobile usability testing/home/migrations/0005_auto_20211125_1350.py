# Generated by Django 2.2.12 on 2021-11-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20211124_1807'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='task_descripttion',
            new_name='task_description',
        ),
    ]
