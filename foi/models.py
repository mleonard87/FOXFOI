from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class CaseManager(models.Manager):
    def create_case(self, title, user):
        case = self.create(title = title, created_date = timezone.now(), created_by = user)
        case.save()
        return case

class CommentManager(models.Manager):
    def create_comment(self, case, subject, body, user):
        comment = self.create(case = case, subject = subject, body = body, created_date = timezone.now(), created_by = user)
        comment.save()
        return comment

class InternalReviewManager(models.Manager):
    def create_internal_review(self, case):
        ir = self.create(case = case)
        ir.save()
        return ir

class InformationCommissionerAppealManager(models.Manager):
    def create_information_commissioner_appeal(self, case):
        ica = self.create(case = case)
        ica.save()
        return ica

class AdministrativeAppealsTribunalManager(models.Manager):
    def create_administrative_appeals_tribunal(self, case):
        aat = self.create(case = case)
        aat.save()
        return aat

class Case(models.Model):
    title = models.CharField(max_length = 100)
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.name

    objects = CaseManager()

class Comment(models.Model):
    case = models.ForeignKey(Case)
    subject = models.CharField(max_length = 100)
    body = models.TextField()
    created_date = models.DateTimeField()
    created_by = models.ForeignKey(User)

    def __unicode__(self):
        return self.subject

    objects = CommentManager()

class InternalReview(models.Model):
    case = models.ForeignKey(Case)
    requested_date = models.DateField(blank = True, null = True)
    review_held_date = models.DateField(blank = True, null = True)
    days_taken_to_hold_review = models.IntegerField(blank = True, null = True)
    review_members = models.TextField(blank = True, null = True)
    review_decision = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return self.case.name

    objects = InternalReviewManager()

class InformationCommissionerAppeal(models.Model):
    case = models.ForeignKey(Case)
    contacted_date = models.DateField(blank = True, null = True)
    documents_provided_date = models.DateField(blank = True, null = True)
    decision_recieved_date = models.DateField(blank = True, null = True)
    decision = models.TextField(blank = True, null = True)
    decision_notice = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.case.name

    objects = InformationCommissionerAppealManager()

class AdministrativeAppealsTribunal(models.Model):
    case = models.ForeignKey(Case)
    contacted_date = models.DateField(blank = True, null = True)
    documents_provided_date = models.DateField(blank = True, null = True)
    decision_recieved_date = models.DateField(blank = True, null = True)
    decision = models.TextField(blank = True, null = True)
    decision_notice = models.CharField(max_length = 100)

    def __unicode__(self):
        return self.case.name

    objects = AdministrativeAppealsTribunalManager()
