# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations
import os, json

def generateMPs(apps, schema_editor):
    # We can't import the MP model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    MP = apps.get_model("mp", "MP")
    mp_list = open(os.path.join(os.path.join(os.path.dirname(__file__), 'migration_data'), 'mp_list.json'))
    mp_json = json.load(mp_list)
    for mp in MP.objects.all():
        mp.delete()
    for mp in mp_json:
        new_mp = MP.objects.create(
            title = mp['title'], 
            name = mp['forename']+' '+mp['surname'], 
            party = mp['party'], 
            constituency = mp['constituency'], 
            address = mp['address'], 
            postcode = mp['postcode'])
        new_mp.save()
    return

class Migration(migrations.Migration):

    dependencies = [
        ('mp', '0002_auto_20150101_1628'),
    ]

    operations = [
        migrations.RunPython(generateMPs),
    ]
