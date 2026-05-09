from django.contrib import admin
from .models import Vehicle, Booking, TechnicalLog

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('marka', 'model', 'vin', 'status') # To pokaże czytelną listę aut
    list_filter = ('status', 'marka') # Pozwoli szybko filtrować auta

admin.site.register(Booking)
admin.site.register(TechnicalLog)