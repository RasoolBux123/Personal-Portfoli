# forms.py
from django import forms
from .models import SocialLink

class SocialForm(forms.ModelForm):
    class Meta:
        model = SocialLink
        fields = ['platform', 'url']
        widgets = {
            'platform': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }
