# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rank', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('given_name', models.CharField(max_length=1000)),
                ('surname', models.CharField(max_length=1000)),
                ('profile', models.CharField(max_length=1000000)),
                ('website', models.CharField(max_length=1000)),
                ('ORCID', models.CharField(max_length=1000)),
                ('is_active', models.BooleanField()),
                ('is_core', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rank', models.CharField(max_length=1000)),
                ('PI', models.ForeignKey(to='members.Faculty')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('rank', models.CharField(max_length=1000)),
                ('PI', models.ForeignKey(to='members.Faculty')),
                ('member', models.ForeignKey(to='members.Member')),
            ],
        ),
        migrations.AddField(
            model_name='faculty',
            name='member',
            field=models.ForeignKey(to='members.Member'),
        ),
    ]
