# Generated by Django 2.0.9 on 2018-11-03 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='expirydate',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 10, 54, 14, 68796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='medicine',
            name='manufacturedate',
            field=models.DateField(default=datetime.datetime(2018, 11, 3, 10, 54, 14, 68796, tzinfo=utc)),
        ),
    ]