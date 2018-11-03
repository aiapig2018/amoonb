# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-01 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20181101_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='body',
            field=models.TextField(db_index=True, max_length=15, verbose_name='分类内容'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='body',
            field=models.TextField(db_index=True, max_length=15, verbose_name='标签内容'),
        ),
    ]
