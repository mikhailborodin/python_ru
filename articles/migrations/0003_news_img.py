# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='img',
            field=models.ImageField(default='/Users/mikhailborodin/Dropbox/python_ru/media/384x256.png', upload_to='news/'),
        ),
    ]
