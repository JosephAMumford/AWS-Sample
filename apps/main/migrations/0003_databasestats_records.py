# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-28 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_databasestats'),
    ]

    operations = [
        migrations.AddField(
            model_name='databasestats',
            name='records',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]