# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 00:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0002_auto_20170531_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='presentation',
            name='paper',
        ),
        migrations.AddField(
            model_name='paper',
            name='presentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meetings.Presentation'),
        ),
    ]
