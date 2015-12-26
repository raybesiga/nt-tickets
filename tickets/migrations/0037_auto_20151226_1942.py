# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-26 19:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0036_auto_20151226_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='FringePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concession_price', models.DecimalField(decimal_places=2, default=5.0, max_digits=6)),
                ('public_price', models.DecimalField(decimal_places=2, default=8.0, max_digits=6)),
                ('member_price', models.DecimalField(decimal_places=2, default=4.0, max_digits=6)),
                ('season_ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Fringe Pricing',
                'verbose_name_plural': 'Fringe Pricing',
            },
        ),
        migrations.CreateModel(
            name='InHousePricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concession_price', models.DecimalField(decimal_places=2, default=5.0, max_digits=6)),
                ('public_price', models.DecimalField(decimal_places=2, default=8.0, max_digits=6)),
                ('member_price', models.DecimalField(decimal_places=2, default=4.0, max_digits=6)),
                ('season_ticket_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('matinee_freshers_price', models.DecimalField(decimal_places=2, default=2.5, max_digits=6)),
                ('matinee_freshers_nnt_price', models.DecimalField(decimal_places=2, default=2.0, max_digits=6)),
            ],
            options={
                'verbose_name': 'In House Pricing',
                'verbose_name_plural': 'In House Pricing',
            },
        ),
        migrations.AddField(
            model_name='sale',
            name='number',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='externalpricing',
            name='concession_price',
            field=models.DecimalField(decimal_places=2, default=5.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='externalpricing',
            name='member_price',
            field=models.DecimalField(decimal_places=2, default=4.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='externalpricing',
            name='public_price',
            field=models.DecimalField(decimal_places=2, default=8.0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='show',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Category'),
        ),
    ]
