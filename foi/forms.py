from django import forms
from django.utils import timezone
from foi.models import Case, Comment, InternalReview, InformationCommissionerAppeal, AdministrativeAppealsTribunal

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = [
            'title', 
            'subject', 
            'received_date', 
            'enquiry_date', 
            'enquiry_ref', 
            'enquiry_method', 
            'response_method', 
            'enquiry_description', 
            'urgent_flag', 
            'handling_instructions',
            'addressee_name']
        labels = {
            'urgent_flag': ('Urgent?')
        }
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': 'Enter a title for this case'}),
            'received_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'enquiry_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'urgent_flag': forms.CheckboxInput(attrs = {'label': 'Urgent?'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['subject', 'body']
        widgets = {
            'subject': forms.TextInput(attrs = {'placeholder': 'Enter a subject for this comment'}),
            'body': forms.Textarea(attrs = {'placeholder': 'Enter a body for this comment'})
        }

class InternalReviewForm(forms.ModelForm):
    class Meta:
        model = InternalReview
        fields = ['requested_date', 'review_held_date', 'days_taken_to_hold_review', 'review_members', 'review_decision']
        widgets = {
            'requested_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'review_held_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()})
        }

class InformationCommissionerAppealForm(forms.ModelForm):
    class Meta:
        model = InformationCommissionerAppeal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']
        widgets = {
            'contacted_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'documents_provided_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'decision_recieved_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()})
        }

class AdministrativeAppealsTribunalForm(forms.ModelForm):
    class Meta:
        model = AdministrativeAppealsTribunal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']
        widgets = {
            'contacted_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'documents_provided_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()}),
            'decision_recieved_date': forms.DateInput(attrs = {'type': 'date', 'value': timezone.now().date()})
        }
