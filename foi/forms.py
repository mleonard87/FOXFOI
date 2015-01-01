from django import forms
from foi.models import Case

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs = {'placeholder': 'Enter a title for this case'})
        }
