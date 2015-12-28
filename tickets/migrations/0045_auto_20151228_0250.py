# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0044_auto_20151227_2244'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Category'),
        ),
    ]
