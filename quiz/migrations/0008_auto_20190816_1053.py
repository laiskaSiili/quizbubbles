# Generated by Django 2.2.4 on 2019-08-16 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0007_auto_20190816_1026'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='finished',
            new_name='active',
        ),
    ]