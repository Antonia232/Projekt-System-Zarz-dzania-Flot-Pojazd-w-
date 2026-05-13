from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['data_start', 'data_koniec']
        widgets = {
            'data_start': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'data_koniec': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }