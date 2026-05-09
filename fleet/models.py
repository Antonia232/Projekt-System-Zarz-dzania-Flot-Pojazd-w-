from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    STATUS_CHOICES = [
        ('dostępny', 'Dostępny'),
        ('naprawa', 'W naprawie'),
        ('zarezerwowany', 'Zarezerwowany'),
    ]
    marka = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vin = models.CharField(max_length=17, unique=True) # VIN musi być unikalny [cite: 189, 236]
    rok = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='dostępny')

    def __str__(self):
        return f"{self.marka} {self.model} ({self.vin})"

class Booking(models.Model):
    pojazd = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    użytkownik = models.ForeignKey(User, on_delete=models.CASCADE)
    data_start = models.DateTimeField()
    data_koniec = models.DateTimeField()

class TechnicalLog(models.Model):
    pojazd = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    przebieg = models.IntegerField()
    opis_naprawy = models.TextField()