# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='picture',
            field=models.ImageField(upload_to='', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='URL',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
    ]
