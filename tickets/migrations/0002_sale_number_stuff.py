# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='number_stuff',
            field=models.IntegerField(default=0),
        ),
    ]