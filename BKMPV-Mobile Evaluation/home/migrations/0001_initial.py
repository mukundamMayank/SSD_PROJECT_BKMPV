# Generated by Django 2.2.12 on 2021-11-24 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connections',
            fields=[
                ('connection_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Observer',
            fields=[
                ('observer_id', models.AutoField(primary_key=True, serialize=False)),
                ('observer_username', models.CharField(max_length=100)),
                ('observer_password', models.CharField(max_length=100)),
                ('observer_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Participants',
            fields=[
                ('participant_id', models.AutoField(primary_key=True, serialize=False)),
                ('participant_email', models.EmailField(max_length=100)),
                ('participant_password', models.CharField(max_length=100)),
                ('participant_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Recordings',
            fields=[
                ('recording_id', models.AutoField(primary_key=True, serialize=False)),
                ('recording_path', models.CharField(max_length=100)),
                ('connections', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Connections')),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('notes_id', models.AutoField(primary_key=True, serialize=False)),
                ('notes_path', models.CharField(max_length=100)),
                ('recordings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Recordings')),
            ],
        ),
        migrations.CreateModel(
            name='Emails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isInvited', models.BooleanField(default=False)),
                ('connections', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Connections')),
            ],
        ),
        migrations.AddField(
            model_name='connections',
            name='participants',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Participants'),
        ),
        migrations.AddField(
            model_name='connections',
            name='tasks',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.Tasks'),
        ),
    ]
