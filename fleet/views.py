from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, Booking
from .forms import BookingForm

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