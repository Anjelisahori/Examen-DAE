from django import forms
from .models import EcoHabit

class EcoHabitForm(forms.ModelForm):
    class Meta:
        model = EcoHabit
        fields = ['nombre', 'descripcion', 'cumplido']
