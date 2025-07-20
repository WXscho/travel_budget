from django.urls import path
# remember the . is due to it being in the current directory

from . import views

urlpatterns = [
  path('hotels/', views.hotel_list, name='hotel_list'),
]