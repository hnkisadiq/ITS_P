# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-13 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20170913_1852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farms',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='farms',
            name='lon',
        ),
        migrations.AddField(
            model_name='farms',
            name='lat1',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='farms',
            name='lat3',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='farms',
            name='lat4',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='farms',
            name='lon1',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='farms',
            name='lon3',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
        migrations.AddField(
            model_name='farms',
            name='lon4',
            field=models.DecimalField(decimal_places=2, default=b'00000', max_digits=5),
        ),
    ]
