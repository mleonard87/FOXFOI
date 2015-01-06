from django import forms
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
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': 'Enter a title for this case'})
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

class InformationCommissionerAppealForm(forms.ModelForm):
    class Meta:
        model = InformationCommissionerAppeal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']

class AdministrativeAppealsTribunalForm(forms.ModelForm):
    class Meta:
        model = AdministrativeAppealsTribunal
        fields = ['contacted_date', 'documents_provided_date', 'decision_recieved_date', 'decision', 'decision_notice']
