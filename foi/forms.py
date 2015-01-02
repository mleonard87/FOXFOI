from django import forms
from foi.models import Case, Comment

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title']
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
