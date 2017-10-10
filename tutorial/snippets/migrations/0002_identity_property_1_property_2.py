# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 16:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adhaar_id', models.IntegerField()),
                ('Name', models.CharField(blank=True, default='Koushik', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Property_1',
            fields=[
                ('house_id', models.AutoField(primary_key=True, serialize=False)),
                ('A_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.Identity')),
            ],
        ),
        migrations.CreateModel(
            name='Property_2',
            fields=[
                ('farm_id', models.AutoField(primary_key=True, serialize=False)),
                ('A_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='snippets.Identity')),
            ],
        ),
    ]
