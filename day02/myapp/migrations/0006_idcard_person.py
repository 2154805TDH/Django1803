# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-10 09:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.CharField(max_length=18, verbose_name='身份证号')),
                ('unite', models.CharField(max_length=30, verbose_name='签发单位')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名字')),
                ('sex', models.CharField(max_length=10, verbose_name='性别')),
                ('idcard', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myapp.IdCard', verbose_name='身份证号')),
            ],
        ),
    ]