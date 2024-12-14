# Generated by Django 2.0.9 on 2018-12-22 22:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDTouch', '0015_auto_20181223_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ambulancebilling',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 4, 11, 25, 627531)),
        ),
        migrations.AlterField(
            model_name='bloodbankcenter',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='qualification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Qualification'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='MDTouch.Specialization'),
        ),
        migrations.AlterField(
            model_name='emergencycontact',
            name='number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 23, 4, 11, 25, 628528)),
        ),
    ]
