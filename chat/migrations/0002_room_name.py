# Generated by Django 2.0 on 2018-03-18 10:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='name',
            field=models.CharField(default=datetime.datetime(2018, 3, 18, 10, 35, 33, 159482, tzinfo=utc), max_length=70),
            preserve_default=False,
        ),
    ]