# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-16 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181012_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(db_index=True, max_length=200, verbose_name='基本信息'),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.CharField(db_index=True, max_length=20, verbose_name='摘要'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(db_index=True, upload_to='products/%Y/%m/%d', verbose_name='背景大图（为了更好地展现，建议宽度1920px，高度600px）'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=25, verbose_name='名称'),
        ),
    ]
