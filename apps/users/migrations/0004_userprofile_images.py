# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-16 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_acritcle'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='images',
            field=models.ImageField(default='', upload_to='user/%Y/%m', verbose_name='头像'),
        ),
    ]
