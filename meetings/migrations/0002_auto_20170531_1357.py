# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='paper',
            field=models.ForeignKey(to='meetings.Paper', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='staff_presenter',
            field=models.ForeignKey(to='members.Staff', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='trainee_presenter',
            field=models.ForeignKey(to='members.Trainee', null=True, blank=True),
        ),
    ]
