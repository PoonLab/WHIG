# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('body', models.CharField(max_length=1000000)),
                ('date', models.DateField(auto_now_add=True)),
                ('lastModified', models.DateField(auto_now=True)),
                ('URL', models.CharField(max_length=1000)),
            ],
        ),
    ]
