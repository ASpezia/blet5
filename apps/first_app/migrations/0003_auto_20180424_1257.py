# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0002_auto_20180424_1156'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pokes',
            new_name='Poke',
        ),
    ]