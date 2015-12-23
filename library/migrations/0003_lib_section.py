# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_lib_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='lib',
            name='section',
            field=models.CharField(null='true', max_length=200),
        ),
    ]
