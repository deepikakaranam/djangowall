# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-24 20:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
