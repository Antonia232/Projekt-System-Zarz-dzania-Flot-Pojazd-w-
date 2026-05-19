from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db.models import Q
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['data_start', 'data_koniec']
        widgets = {
            'data_start': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'data_koniec': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

   
    def __init__(self, *args, **kwargs):
        self.pojazd = kwargs.pop('pojazd', None)
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        data_start = cleaned_data.get('data_start')
        data_koniec = cleaned_data.get('data_koniec')

        if data_start and data_koniec:
            
            if data_start < timezone.now():
                raise ValidationError("Data rozpoczęcia nie może być w przeszłości!")

            if data_koniec <= data_start:
                raise ValidationError("Data zakończenia rezerwacji musi być późniejsza niż data rozpoczęcia!")

            
            if self.pojazd:
                overlapping_bookings = Booking.objects.filter(
                    pojazd=self.pojazd
                ).filter(
                    Q(data_start__lt=data_koniec) & Q(data_koniec__gt=data_start)
                )

                if overlapping_bookings.exists():
                    raise ValidationError("Ten pojazd jest już zarezerwowany w tym terminie! Wybierz inne daty.")

        return cleaned_data