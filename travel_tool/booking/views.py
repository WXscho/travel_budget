from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, get_object_or_404
import json
import requests
from .models import Hotel, Room
from django.conf import settings


import logging
logger = logging.getLogger(__name__)

# Create your views here.
# for when I get money to try out full functionality of API


def map_view(request):
  return render(request, 'map.html')

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