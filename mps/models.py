from django.db import models
from django.db.models import Q

class MPManager(models.Manager):
    def create_mp(self, title, name, party, constituency, address, postcode):
        mp = self.create(title = title, name = name, party = party, constituency = constituency, address = address, postcode = postcode)
        mp.save()
        return mp

    def search_mps(self, search_term):
        if search_term != None:
            q = Q(title__icontains = search_term) 
            q |= Q(name__icontains = search_term) 
            q |= Q(party__icontains = search_term) 
            q |= Q(constituency__icontains = search_term) 
            q |= Q(address__icontains = search_term) 
            q |= Q(postcode__icontains = search_term)

            return self.filter(q).order_by('name')

        return self.order_by('name')

class MP(models.Model):
    title = models.CharField(max_length = 20)
    name = models.CharField(max_length = 100)
    party = models.CharField(max_length = 100)
    constituency = models.CharField(max_length = 100)
    address = models.CharField(max_length = 400, blank = True)
    postcode = models.CharField(max_length = 10, blank = True)

    objects = MPManager()
