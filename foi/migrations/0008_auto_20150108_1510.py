# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0007_assessment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment',
            name='third_party_contact_name',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessment',
            name='third_party_contact_telephone',
            field=models.CharField(default=b'', max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assessment',
            name='third_party_request_general_description',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
    ]
