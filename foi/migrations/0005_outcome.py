# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0004_auto_20150106_2146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Outcome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('foi_outcomes', models.CharField(max_length=100, choices=[(b'FULL_ACCESS', b'1) Grant access in full'), (b'PARTIAL_EXEMPTION', b'2) Withhold some documents as exempt'), (b'FULL_EXEMPTION', b'3) Withhold all documents as exempt'), (b'DEFER', b'4) Defer access'), (b'REDACTION', b'5) Grant access with redactions'), (b'DNE', b'6) Documents do not exist or cannot be found'), (b'NCND', b'7) Neither confirm nor deny')])),
                ('foi_exemptions', models.CharField(max_length=100, choices=[(b'CSR', b'Commonwealth-State Relations'), (b'DPRAMF', b'Deliberative Processes Relating to Agencies or Ministers Functions'), (b'FPIC', b'Financial and Property Interests of the Commonwealth'), (b'OAM', b'Operations of Agencies Management'), (b'PP', b'Personal Privacy'), (b'BA', b'Business Affairs'), (b'RCANU', b'Research by CSIRO or the Australian National University'), (b'AE', b'Australias Economy')])),
                ('foi_conditional_exemptions', models.CharField(max_length=100, choices=[(b'CSR', b'Commonwealth-State Relations'), (b'DPRAMF', b'Deliberative Processes Relating to Agencies or Ministers Functions'), (b'FPIC', b'Financial and Property Interests of the Commonwealth'), (b'OAM', b'Operations of Agencies Management'), (b'PP', b'Personal Privacy'), (b'BA', b'Business Affairs'), (b'RCANU', b'Research by CSIRO or the Australian National University'), (b'AE', b'Australias Economy')])),
                ('disclosure_outcomes', models.CharField(max_length=100, choices=[(b'GRANTED_IN_FULL', b'Granted In Full'), (b'WITHHELD_IN_PART', b'Withheld In Part'), (b'WITHHELD_IN_FULL', b'Withheld In Full')])),
                ('certificates', models.CharField(max_length=100, choices=[(b'National Security', b'National Security'), (b'Defence', b'Defence'), (b'International Relations', b'International Relations'), (b'Relations with States', b'Relations with States'), (b'Cabinet Documents', b'Cabinet Documents'), (b'Executive Council Documents', b'Executive Council Documents'), (b'Internal Working Documents', b'Internal Working Documents')])),
                ('case', models.ForeignKey(to='foi.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
