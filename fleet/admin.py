from django.contrib import admin
from .models import Vehicle, Booking, TechnicalLog


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('marka', 'model', 'vin', 'status') # przykładowe pola
    search_fields = ('vin', 'marka')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass

@admin.register(TechnicalLog)
class TechnicalLogAdmin(admin.ModelAdmin):
    pass

