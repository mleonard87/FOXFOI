from django import forms
from mp.models import MP

class MPForm(forms.ModelForm):
    class Meta:
        model = MP
        fields = ['title', 'name', 'party', 'constituency', 'address', 'postcode']
