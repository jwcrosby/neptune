# Generated by Django 3.2.6 on 2021-08-29 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0030_alter_buddy_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddy',
            name='icon',
            field=models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=1, null=True, verbose_name='Icon'),
        ),
    ]
