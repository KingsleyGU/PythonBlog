# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_hahas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hahas',
            new_name='Comments',
        ),
    ]
