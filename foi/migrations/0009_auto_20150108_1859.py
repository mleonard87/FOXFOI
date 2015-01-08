# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0008_auto_20150108_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='enquirer_address',
            field=models.CharField(default=b'', max_length=400, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_department',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_email_address',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_enquirer_group',
            field=models.CharField(default=b'', max_length=10, blank=True, choices=[(b'A', b'Academia'), (b'B', b'Businesses'), (b'C', b'Charities/Lobby Groups'), (b'E', b'Employees'), (b'M', b'Media'), (b'MP', b'MPs'), (b'P', b'Public'), (b'O', b'Other Govt body/Local Authority/etc.')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_industry_body',
            field=models.CharField(default=b'', max_length=10, blank=True, choices=[(b'NR', b'Transport - Roads'), (b'FSR', b'Transport - Rail'), (b'TPE', b'Transport - Air'), (b'GEXP', b'Utilities - Gas'), (b'GC', b'Utilities - Electricity'), (b'HE', b'Utilities - Water'), (b'HT', b'Chemicals - Household'), (b'IL', b'Chemicals - Industrial'), (b'LM', b'Financial - Banking'), (b'LU', b'Financial - Insurance'), (b'MR', b'Financial - Investments'), (b'XC', b'Catering'), (b'NR', b'Hospitality'), (b'NXEA', b'Communications - IT'), (b'NXEC', b'Communications - Mobile'), (b'SE', b'Communications - Landlines/Cable'), (b'SR', b'Energy - Wind'), (b'SWT', b'Energy - Water'), (b'SEXP', b'Energy - Nuclear'), (b'WSMR', b'Energy - Oil and Gas'), (b'VT', b'Media - Satellite'), (b'DLR', b'Media - Press'), (b'ATW', b'Media - TV and Radio'), (b'TFL', b'TFL - Bus'), (b'SPTE', b'TFL - Underground'), (b'TW', b'Agriculture - Industrial'), (b'TRAM', b'Agriculture - Farming'), (b'HR', b'Government - Environment'), (b'ATOC', b'Government - Educational'), (b'DFT', b'Government - Transport'), (b'ORR', b'Government - Financial'), (b'ROSCO', b'Government - Social'), (b'TL', b'Retail - Department Stores'), (b'C2C', b'Retail - Independent'), (b'OTHER', b'Retail - Food'), (b'SOME_', b'Other'), (b'CR', b'EU'), (b'EMT', b'Far East'), (b'ES', b'US'), (b'FCC', b'African'), (b'FGW', b'Southern Hemisphere')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_name',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_organisation',
            field=models.CharField(default=b'', max_length=100, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_postcode',
            field=models.CharField(default=b'', max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_region',
            field=models.CharField(default=b'', max_length=10, blank=True, choices=[(b'LO', b'London'), (b'MI', b'Midlands'), (b'NE', b'North East'), (b'NW', b'North West'), (b'SC', b'Scotland'), (b'SO', b'South'), (b'SE', b'South East'), (b'SW', b'South West'), (b'WA', b'Wales')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_telephone',
            field=models.CharField(default=b'', max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='case',
            name='enquirer_title',
            field=models.CharField(default=b'', max_length=20, blank=True),
            preserve_default=True,
        ),
    ]
