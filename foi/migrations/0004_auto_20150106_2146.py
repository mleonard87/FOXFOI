# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0003_administrativeappealstribunal_informationcommissionerappeal_internalreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='addressee_name',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquiry_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquiry_description',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquiry_method',
            field=models.CharField(default=b'', max_length=20, blank=True, choices=[(b'EMAIL', b'Email'), (b'LETTER', b'Letter'), (b'PHONE', b'Phone'), (b'FAX', b'Fax')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquiry_ref',
            field=models.CharField(default=b'', max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='handling_instructions',
            field=models.CharField(default=b'', max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='received_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='response_method',
            field=models.CharField(default=b'', max_length=20, blank=True, choices=[(b'EMAIL', b'Email'), (b'LETTER', b'Letter'), (b'PHONE', b'Phone'), (b'FAX', b'Fax')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='subject',
            field=models.CharField(default=b'', max_length=250, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='urgent_flag',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
