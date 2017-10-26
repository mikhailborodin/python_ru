# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 16:06
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=100)),
                ('preview', models.CharField(max_length=255)),
                ('text', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'новость',
                'verbose_name_plural': 'новости',
            },
        ),
    ]
