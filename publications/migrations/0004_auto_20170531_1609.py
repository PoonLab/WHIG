# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_publication_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='URL',
            field=models.CharField(max_length=1000),
        ),
    ]
