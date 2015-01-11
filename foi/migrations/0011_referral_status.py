# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0010_referral'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='status',
            field=models.CharField(default=b'OPEN', max_length=10, choices=[(b'OPEN', b'Open'), (b'CLOSED', b'Closed')]),
            preserve_default=True,
        ),
    ]
