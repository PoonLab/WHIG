# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170531_1357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='picture',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/DefaultImage.png', upload_to='images/', null=True, blank=True),
        ),
    ]
