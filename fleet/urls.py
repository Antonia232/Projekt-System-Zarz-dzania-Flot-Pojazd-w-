from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('dashboard/', views.user_dashboard, name='dashboard'),
    path('manager-fleet/', views.admin_dashboard, name='admin_dashboard'),  # <-- TO DOPISUJEMY
]