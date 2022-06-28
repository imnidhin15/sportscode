from django import forms
from .models import event

class Sportsform(forms.ModelForm):
    class Meta:
        model = event
        fields = ['name', 'description', 'team', 'image']