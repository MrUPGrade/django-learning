# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0002_auto_20171108_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile'),
        ),
    ]
