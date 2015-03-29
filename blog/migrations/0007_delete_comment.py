# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150329_1853'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
