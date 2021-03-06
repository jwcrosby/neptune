# Generated by Django 3.2.6 on 2021-08-27 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0020_auto_20210826_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buddy',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 16, 55, 51, 682206, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dive',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 16, 55, 51, 682875, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='note',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 16, 55, 51, 683960, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 16, 55, 51, 684426, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='trip',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 27, 16, 55, 51, 681378, tzinfo=utc)),
        ),
    ]
