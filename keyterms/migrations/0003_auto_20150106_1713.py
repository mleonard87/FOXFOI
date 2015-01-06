# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('keyterms', '0002_auto_20150106_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keyterm',
            name='name',
            field=models.CharField(unique=True, max_length=50, error_messages={b'unique': b'A Key Term already exists with this name'}),
            preserve_default=True,
        ),
    ]
