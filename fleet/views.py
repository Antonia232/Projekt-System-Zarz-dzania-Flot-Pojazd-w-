from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, CreateView 
from django.db.models import Sum
from .models import Vehicle, Booking

# fleet/views.py
from .mixins import ManagerRequiredMixin, DriverRequiredMixin

class ReportView(ManagerRequiredMixin, ListView):
    # Tylko Managerowie zobaczą raporty
    model = Vehicle
    template_name = 'fleet/report.html'

class BookingCreateView(DriverRequiredMixin, CreateView):
    # Tylko Kierowcy mogą tworzyć rezerwacje
    model = Booking
    ...

    
#1 Lista samochodów
class VehicleListView(ListView):
    model = Vehicle
    template_name = 'fleet/vehicle_list.html'
    context_object_name = 'vehicles'

#2 Formularz rezerwacji 
class BookingCreateView(CreateView):
    model = Booking
    fields = ['vehicle', 'start_date', 'end_date']
    success_url = '/moje rezerwacje/' 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
#3 Raport (Agregacja ORM)
class ReportView(LoginRequiredMixin, ManagerRequiredMixin, Listview):
    model = Vehicle
    template_name = 'fleet/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_mileage'] = Vehicle.objects.aggregate(total=Sum('mileage'))['total']
        return context