from django import forms
from mps.models import MP

class MPForm(forms.ModelForm):
    class Meta:
        model = MP
        fields = ['title', 'name', 'party', 'constituency', 'address', 'postcode']
