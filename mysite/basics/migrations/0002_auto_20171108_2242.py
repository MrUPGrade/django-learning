# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-08 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='contacts', to='basics.Tag'),
        ),
    ]
