# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0006_auto_20150107_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('third_party_consultation', models.BooleanField(default=False)),
                ('precedents', models.BooleanField(default=False)),
                ('precedent_details', models.TextField(null=True, blank=True)),
                ('fee_flag', models.BooleanField(default=False)),
                ('search_and_retrieval_time', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('decision_making_time', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('photocopy_charges', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('other_access_time', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('postage_charges', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('initial_deposit', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
                ('include_refine_request_flag', models.BooleanField(default=False)),
                ('include_third_party_consultation_flag', models.BooleanField(default=False)),
                ('request_concerning', models.CharField(blank=True, max_length=100, choices=[(b'PERSON_BUSINESS', b'a persons business or professional affairs'), (b'ORGANISATION_BUSINESS', b'an organisations business or professional affairs'), (b'PERSON_PERSONAL', b'an individuals personal information'), (b'GOVERNMENT', b'material originating or received from a State or Territory government'), (b'FOREIGN', b'material originating or received from a foreign entity')])),
                ('fee_notice_issued_flag', models.BooleanField(default=False)),
                ('fee_notice_issued_date', models.DateField(null=True, blank=True)),
                ('fee_payment_required_date', models.DateField(null=True, blank=True)),
                ('fee_paid_flag', models.BooleanField(default=False)),
                ('fee_received_date', models.DateField(null=True, blank=True)),
                ('fee_limit_flag', models.BooleanField(default=False)),
                ('request_general_description', models.CharField(max_length=100, blank=True)),
                ('documents_attached_or_described', models.CharField(blank=True, max_length=100, choices=[(b'ATTACHED', b'Attached'), (b'DESCRIBED', b'Described')])),
                ('include_s47_flag', models.BooleanField(default=False)),
                ('include_s47b_flag', models.BooleanField(default=False)),
                ('include_s47f_flag', models.BooleanField(default=False)),
                ('include_s47g_flag', models.BooleanField(default=False)),
                ('respond_by_date', models.DateField(null=True, blank=True)),
                ('contact_name', models.CharField(max_length=100, blank=True)),
                ('contact_telephone', models.CharField(max_length=30, blank=True)),
                ('third_party_title', models.CharField(max_length=20, blank=True)),
                ('third_party_name', models.CharField(max_length=100, blank=True)),
                ('third_party_department', models.CharField(max_length=100, blank=True)),
                ('third_party_organisation', models.CharField(max_length=100, blank=True)),
                ('third_party_address', models.CharField(max_length=400, blank=True)),
                ('third_party_postcode', models.CharField(max_length=10, blank=True)),
                ('case', models.ForeignKey(to='foi.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
