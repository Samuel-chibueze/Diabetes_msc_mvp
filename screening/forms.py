from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient

        fields = [
            'gender',
            'age',
            'bmi',
            'blood_pressure',
            'glucose_level',
            'family_history'
        ]