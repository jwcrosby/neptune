# Generated by Django 3.2.6 on 2021-08-26 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20210826_1100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
