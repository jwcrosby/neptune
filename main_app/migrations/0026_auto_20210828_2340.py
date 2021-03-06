# Generated by Django 3.2.6 on 2021-08-28 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0025_auto_20210828_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dive',
            name='geeks_field',
        ),
        migrations.AddField(
            model_name='dive',
            name='acc_bottom_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Accumulated Bottom Time (min)'),
        ),
        migrations.AddField(
            model_name='dive',
            name='bottom_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bottom Time (min)'),
        ),
        migrations.AddField(
            model_name='dive',
            name='purpose',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Purpose'),
        ),
        migrations.AddField(
            model_name='dive',
            name='safety_stop_depth',
            field=models.IntegerField(blank=True, null=True, verbose_name='Safety Stop Depth (ft)'),
        ),
        migrations.AddField(
            model_name='dive',
            name='safety_stop_time',
            field=models.IntegerField(blank=True, null=True, verbose_name='Safety Stop Time (min)'),
        ),
        migrations.AddField(
            model_name='dive',
            name='suit_desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Suit Description'),
        ),
        migrations.AddField(
            model_name='dive',
            name='suit_notes',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Additional Suit Notes'),
        ),
        migrations.AddField(
            model_name='dive',
            name='suit_thickness',
            field=models.IntegerField(blank=True, null=True, verbose_name='Thickness (mm)'),
        ),
        migrations.AddField(
            model_name='dive',
            name='weather',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Weather'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='depth_avg',
            field=models.IntegerField(blank=True, null=True, verbose_name='Average Depth (ft)'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='depth_max',
            field=models.IntegerField(blank=True, null=True, verbose_name='Max Depth (ft)'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='temperature_air',
            field=models.IntegerField(blank=True, null=True, verbose_name='Air Temperature (F)'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='temperature_bottom',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bottom Temperature (F)'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='temperature_surface',
            field=models.IntegerField(blank=True, null=True, verbose_name='Surface Temperature (F)'),
        ),
        migrations.AlterField(
            model_name='dive',
            name='visibility',
            field=models.IntegerField(blank=True, null=True, verbose_name='Visbility (ft)'),
        ),
    ]
