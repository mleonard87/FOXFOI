# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mp',
            name='address',
            field=models.CharField(max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='mp',
            name='postcode',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
