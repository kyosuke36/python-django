# Generated by Django 5.1.2 on 2024-12-12 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_choice_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='choice_text',
            field=models.CharField(max_length=200),
        ),
    ]
