from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Hotel, Room
from django.conf import settings


import logging
logger = logging.getLogger(__name__)

# Create your views here.
# for when I get money to try out full functionality of API


#    <!-- Watch youtube video and take it step by step-->

def hotel_list(request):
  hotels = Hotel.objects.all()
  return render(request, 'hotels.html', {'hotels': hotels})

def home_page(request):
  return render(request, 'home.html')

def hotel_item(request, hotel_id):
  hotel = get_object_or_404(Hotel,pk=hotel_id)
  return render(request, 'hotel_detail.html',{'hotel': hotel})

def room_list(request, hotel_id):
  hotel =get_object_or_404(Hotel,pk=hotel_id)
  rooms = hotel.rooms.all()
  return render(request, 'rooms.html', {'hotel': hotel, 'rooms': rooms})
def map_view(request):
  return render(request, "map.html")