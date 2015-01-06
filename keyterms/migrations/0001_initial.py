# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KeyTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20, error_messages={b'unique': b'A Key Term already exists with this name'})),
                ('status', models.CharField(max_length=1, choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
                ('parent', models.ForeignKey(blank=True, to='keyterms.KeyTerm', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
