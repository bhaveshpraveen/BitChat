# Generated by Django 2.0 on 2018-03-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20180318_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['created']},
        ),
    ]