from django import forms

from django import forms
from .models import Pin, Location


class PinForm(forms.ModelForm):
    class Meta:
        model = Pin
        fields = ['title', 'location', 'year', 'designer', 'note', 'played']
        labels = {'title': 'title'}

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'address', 'notes']