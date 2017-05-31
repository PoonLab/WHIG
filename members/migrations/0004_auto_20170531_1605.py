# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='picture',
        ),
        migrations.AddField(
            model_name='member',
            name='image',
            field=models.ImageField(upload_to='images/', default='images/DefaultImage.png', blank=True, null=True),
        ),
    ]
