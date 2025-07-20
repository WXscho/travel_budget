from django.urls import path
# remember the . is due to it being in the current directory

from . import views

urlpatterns = [
  path('', views.home_page, name='home-page'),
  path('hotels/', views.hotel_list, name='hotel-list'),
  path('hotels/<int:hotel_id>', views.hotel_item, name='hotel-detail'),
]