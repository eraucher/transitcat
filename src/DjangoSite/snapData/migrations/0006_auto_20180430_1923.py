# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-01 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snapData', '0005_auto_20180430_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snappickle',
            name='pickleFileName',
            field=models.FilePathField(default=b'', match=b'*.pkl', path=b'snapData/uploads'),
        ),
        migrations.AlterField(
            model_name='snappickle',
            name='snapFileName',
            field=models.FilePathField(default=b'', match=b'*.graph', path=b'snapData/uploads'),
        ),
    ]
