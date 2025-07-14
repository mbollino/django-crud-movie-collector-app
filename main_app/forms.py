from django import forms
from .models import Viewing

class ViewingForm(forms.ModelForm):
    class Meta:
        model = Viewing
        fields = ['view_date', 'personal_rating']
        widgets = {
            'view_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a date',
                    'type': 'date',
                }
            ),
        }
