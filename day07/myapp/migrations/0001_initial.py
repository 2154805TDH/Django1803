# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-17 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='游戏名字')),
                ('desc', models.CharField(max_length=251, verbose_name='简介')),
                ('rate', models.FloatField(verbose_name='评分')),
            ],
        ),
    ]
