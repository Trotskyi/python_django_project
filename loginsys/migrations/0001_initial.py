# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 15:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Logger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('type', models.CharField(choices=[('C', 'Created'), ('M', 'Modified'), ('D', 'Deleted')], max_length=1, verbose_name='Type')),
                ('model', models.CharField(max_length=200, verbose_name='Class')),
                ('log', models.CharField(max_length=250, verbose_name='Log')),
            ],
        ),
    ]
