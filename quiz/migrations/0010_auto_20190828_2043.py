# Generated by Django 2.2.4 on 2019-08-28 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_bubble_last_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bubble',
            old_name='last_update',
            new_name='last_contribution',
        ),
    ]
