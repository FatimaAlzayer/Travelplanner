from django.shortcuts import render
from .models import Trip, Activity, Member
def home(request):
    return render(request, 'trips/home.html')

def trip_list(request):
    trips=Trip.objects.all()


