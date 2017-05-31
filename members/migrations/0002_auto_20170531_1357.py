# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='faculty',
            options={'verbose_name': 'Faculty', 'verbose_name_plural': 'Faculty'},
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'verbose_name': 'Staff', 'verbose_name_plural': 'Staff'},
        ),
        migrations.AddField(
            model_name='member',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='member',
            name='ORCID',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='website',
            field=models.CharField(max_length=1000, blank=True, null=True),
        ),
    ]
