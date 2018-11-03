# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20181016_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='背景大图（为了更好地展现，建议宽度1920px，高度600px）'),
        ),
        migrations.AddField(
            model_name='tag',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='背景大图（为了更好地展现，建议宽度1920px，高度600px）'),
        ),
    ]