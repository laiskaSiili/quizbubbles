# Generated by Django 2.2.4 on 2019-08-21 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20190821_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='increment_duration_at_roundstart',
        ),
        migrations.AddField(
            model_name='game',
            name='timestop_active',
            field=models.BooleanField(default=False),
        ),
    ]
