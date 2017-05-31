# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='faculty',
            field=models.ForeignKey(null=True, to='members.Faculty', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='staff',
            field=models.ForeignKey(null=True, to='members.Staff', blank=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='trainee',
            field=models.ForeignKey(null=True, to='members.Trainee', blank=True),
        ),
    ]
