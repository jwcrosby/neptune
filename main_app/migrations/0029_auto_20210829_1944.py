# Generated by Django 3.2.6 on 2021-08-29 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0028_alter_dive_acc_bottom_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buddy',
            name='color',
        ),
        migrations.AddField(
            model_name='buddy',
            name='icon',
            field=models.CharField(blank=True, choices=[('A', 'Air'), ('N', 'Nitrox')], default='A', max_length=1, null=True, verbose_name='Icon'),
        ),
    ]