# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 08:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20171208_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinfo',
            name='icp',
            field=models.CharField(default='', help_text='ICP', max_length=20, verbose_name='ICP'),
        ),
    ]