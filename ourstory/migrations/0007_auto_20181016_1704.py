# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourstory', '0006_remove_article_storycontent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(db_index=True, upload_to='ourstory/%Y/%m/%d', verbose_name='背景图'),
        ),
    ]
