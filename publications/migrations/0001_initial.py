# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('authors_line', models.CharField(max_length=1000)),
                ('faculty', models.ForeignKey(to='members.Faculty')),
                ('staff', models.ForeignKey(to='members.Staff')),
                ('trainee', models.ForeignKey(to='members.Trainee')),
            ],
        ),
    ]
