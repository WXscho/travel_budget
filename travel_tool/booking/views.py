from django.shortcuts import render, get_object_or_404
from .models import Hotel
# Create your views here.


def hotel_list(request):
  hotels = Hotel.objects.all()
  return render(request, 'hotels.html', {'hotels': hotels})

def home_page(request):
  return render(request, 'home.html')

def hotel_item(request, hotel_id):
  hotel = get_object_or_404(Hotel,pk=hotel_id)
  return render(request, 'hotel_detail.html',{'hotel': hotel})

