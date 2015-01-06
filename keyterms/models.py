from django.db import models
from django.core.exceptions import ValidationError

class KeyTermManager(models.Manager):
    def create_key_term(self, name, parent):
        kt = self.create(name = name, status = 'ACTIVE', parent = parent)
        kt.save()
        return kt

    def get_parent_key_terms(self):
        kts = self.filter(parent = None).order_by('name')
        return kts

class KeyTerm(models.Model):

    STATUS = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive')
    )

    name = models.CharField(max_length = 20, unique = True, error_messages={'unique': 'A Key Term already exists with this name'})
    status = models.CharField(max_length = 10, choices = STATUS)
    parent = models.ForeignKey('self', null = True, blank = True)

    def change_status(self):
        self.status = 'INACTIVE' if self.status == 'ACTIVE' else 'ACTIVE'
        if self.parent != None and self.parent.status == 'INACTIVE' and self.status == 'ACTIVE':
            self.parent.change_status()
        if self.parent == None:
            for child in self.sortedKeyTerms():
                if child.status == 'ACTIVE':
                    child.change_status()
        self.save()

    def is_active(self):
        return True if self.status == 'ACTIVE' else False

    def sortedKeyTerms(self):
        return self.keyterm_set.order_by('name')

    def clean(self):
        parent_kt = self.parent
        if parent_kt != None:
            if parent_kt.parent != None:
                raise ValidationError('Parent Key Terms must not have parents')

    objects = KeyTermManager()
