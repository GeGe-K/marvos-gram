# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-14 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='ids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=30)),
            ],
        ),
    ]