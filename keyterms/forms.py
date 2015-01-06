from django import forms
from keyterms.models import KeyTerm

class KeyTermForm(forms.ModelForm):
    class Meta:
        model = KeyTerm
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs = {'placeholder': 'Enter a name for this Key Term'})
        }
