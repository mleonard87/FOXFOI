# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keyterms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyterm',
            name='status',
            field=models.CharField(max_length=10, choices=[(b'ACTIVE', b'Active'), (b'INACTIVE', b'Inactive')]),
            preserve_default=True,
        ),
    ]
