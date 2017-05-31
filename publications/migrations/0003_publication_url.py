# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0002_auto_20170531_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='URL',
            field=models.CharField(max_length=1000, default=''),
        ),
    ]
