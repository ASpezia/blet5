# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-24 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pokes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('poked', models.ManyToManyField(related_name='pokers', to='first_app.pokes')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='Friend',
        ),
    ]
