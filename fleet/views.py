from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, Booking
from .forms import BookingForm

<<<<<<< HEAD
# DODAJ TĘ FUNKCJĘ TUTAJ:
def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'fleet/index.html', {'vehicles': vehicles})

# TWOJA ISTNIEJĄCA FUNKCJA (zostaje bez zmian):
def car_detail(request, car_id):
    car = get_object_or_404(Vehicle, id=car_id)
    # ... reszta kodu, którą już masz ...
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.pojazd = car
            booking.użytkownik = request.user
            booking.save()
            
            car.status = 'zarezerwowany'
            car.save()
            return redirect('index')
    else:
        form = BookingForm()
        
    return render(request, 'fleet/car_detail.html', {'car': car, 'form': form})
=======
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
>>>>>>> 0ca26624c357b81ded5626f270229fc1aa701169
