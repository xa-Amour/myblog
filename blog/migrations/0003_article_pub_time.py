# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-02-13 09:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190201_0848'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
