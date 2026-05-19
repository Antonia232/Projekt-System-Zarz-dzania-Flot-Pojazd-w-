from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Vehicle, Booking
from .forms import BookingForm


def index(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'fleet/index.html', {'vehicles': vehicles})

@login_required
def car_detail(request, car_id):
    car = get_object_or_404(Vehicle, id=car_id)
    if request.method == 'POST':
        
        form = BookingForm(request.POST, pojazd=car)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.pojazd = car
            booking.użytkownik = request.user
            booking.save()
            return redirect('index')
    else:
       
        form = BookingForm(pojazd=car)
        
    return render(request, 'fleet/car_detail.html', {'car': car, 'form': form})
@login_required
def user_dashboard(request):

    moje_rezerwacje = Booking.objects.filter(użytkownik=request.user).order_by('-data_start')
    
    return render(request, 'fleet/dashboard.html', {
        'bookings': moje_rezerwacje
    })
@login_required
def admin_dashboard(request):
    
    wszystkie_auta = Vehicle.objects.all().order_by('marka')
    
    return render(request, 'fleet/admin_dashboard.html', {
        'vehicles': wszystkie_auta
    })