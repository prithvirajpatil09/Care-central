# Generated by Django 2.0.9 on 2018-12-12 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0011_auto_20181212_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescription',
            name='prescription',
            field=models.CharField(default='', max_length=800, null=True),
        ),
        migrations.AlterField(
            model_name='ambulancebilling',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 12, 17, 48, 25, 377644)),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.ManyToManyField(to='MDTouch.Qualification'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ManyToManyField(to='MDTouch.Specialization'),
        ),
    ]