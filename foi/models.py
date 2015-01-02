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