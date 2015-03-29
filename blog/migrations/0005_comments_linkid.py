# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150329_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='linkid',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
