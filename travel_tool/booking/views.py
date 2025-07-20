from django.shortcuts import render
from .models import Hotel
# Create your views here.


def hotel_list(request):
  hotels= Hotel.objects.all()
  return render(request, 'hotels.html', {'hotels': hotels})


