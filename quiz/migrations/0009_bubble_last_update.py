# Generated by Django 2.2.4 on 2019-08-28 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0008_remove_quiz_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='bubble',
            name='last_update',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
