# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 15:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_section_template_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='content',
        ),
    ]
