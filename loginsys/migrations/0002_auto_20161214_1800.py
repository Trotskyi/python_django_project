# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 16:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Logger',
            new_name='Loginsys',
        ),
    ]
