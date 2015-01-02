# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foi', '0002_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeAppealsTribunal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacted_date', models.DateField(null=True, blank=True)),
                ('documents_provided_date', models.DateField(null=True, blank=True)),
                ('decision_recieved_date', models.DateField(null=True, blank=True)),
                ('decision', models.TextField(null=True, blank=True)),
                ('decision_notice', models.CharField(max_length=100)),
                ('case', models.ForeignKey(to='foi.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InformationCommissionerAppeal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contacted_date', models.DateField(null=True, blank=True)),
                ('documents_provided_date', models.DateField(null=True, blank=True)),
                ('decision_recieved_date', models.DateField(null=True, blank=True)),
                ('decision', models.TextField(null=True, blank=True)),
                ('decision_notice', models.CharField(max_length=100)),
                ('case', models.ForeignKey(to='foi.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InternalReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('requested_date', models.DateField(null=True, blank=True)),
                ('review_held_date', models.DateField(null=True, blank=True)),
                ('days_taken_to_hold_review', models.IntegerField(null=True, blank=True)),
                ('review_members', models.TextField(null=True, blank=True)),
                ('review_decision', models.TextField(null=True, blank=True)),
                ('case', models.ForeignKey(to='foi.Case')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
