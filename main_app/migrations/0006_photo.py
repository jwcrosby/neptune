# Generated by Django 3.2.4 on 2021-08-26 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_dive_buddies'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('dive', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main_app.dive')),
            ],
        ),
    ]