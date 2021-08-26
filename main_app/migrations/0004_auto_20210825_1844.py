# Generated by Django 3.2.4 on 2021-08-26 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20210825_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buddy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dive',
            options={'ordering': ['-number']},
        ),
    ]