# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_auto_20170603_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=models.ImageField(default='./members/static/members/DefaultImage.png', upload_to='./members/static/members'),
        ),
    ]
