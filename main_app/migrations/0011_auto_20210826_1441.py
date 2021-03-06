# Generated by Django 3.2.6 on 2021-08-26 20:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20210826_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dive',
            old_name='location',
            new_name='site',
        ),
        migrations.AddField(
            model_name='dive',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dive',
            name='number',
            field=models.IntegerField(verbose_name='#'),
        ),
    ]
