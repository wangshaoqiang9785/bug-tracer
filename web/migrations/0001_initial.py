# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-07-30 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, verbose_name='用户名')),
                ('email', models.EmailField(max_length=32, verbose_name='邮箱')),
                ('mobile_phone', models.CharField(max_length=32, verbose_name='手机号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
            ],
        ),
    ]
