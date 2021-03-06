# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-05 02:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0003_auto_20180704_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField(default=1, verbose_name='商品数量')),
                ('is_selected', models.BooleanField(default=True, verbose_name='选中状态')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='axf.Goods', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
    ]
