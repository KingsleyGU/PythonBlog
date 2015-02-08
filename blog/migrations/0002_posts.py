# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import blog.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=150)),
                ('src', models.ImageField(upload_to=blog.models.get_upload_file_name)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
