# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 16:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_news_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='large',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='news',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='img',
            field=models.ImageField(upload_to='news/'),
        ),
    ]