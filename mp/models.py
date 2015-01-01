from django.db import models

class MPManager(models.Manager):
    def create_mp(self, title, name, party, constituency, address, postcode):
        mp = self.create(title = title, name = name, party = party, constituency = constituency, address = address, postcode = postcode)
        mp.save()
        return mp

class MP(models.Model):
    title = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    party = models.CharField(max_length = 100)
    constituency = models.CharField(max_length = 100)
    address = models.CharField(max_length = 400, blank = True)
    postcode = models.CharField(max_length = 10, blank = True)

    objects = MPManager()
