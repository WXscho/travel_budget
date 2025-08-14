from django.db import models
from django_google_maps import fields as map_fields
# Create your models here.

#

# Hotel metadata model
class Hotel(models.Model):
  hotel_id = models.AutoField(primary_key=True)
  hotel_name = models.CharField(max_length=100)
  hotel_address = models.CharField(max_length=100)
  hotel_city = models.CharField(max_length=100)
  hotel_state = models.CharField(max_length=100)
  hotel_zip = models.CharField(max_length=11)
  hotel_rated= models.DecimalField(decimal_places=1,
                                   max_digits=2,
                                   choices=[(x/2, f"{x/2}") for x in range(2,11)]
                                   )
  def __str__(self):
    return f"{self.hotel_name} {self.hotel_rated} Stars"
# Room Model: for every room in a hotel
class Room(models.Model):
  room_id = models.AutoField(primary_key=True)
  room_type = models.CharField(max_length=100)
  room_duration = models.DecimalField(decimal_places=1, max_digits=2)
  room_cost = models.DecimalField(decimal_places=2, max_digits=7)
  hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name="rooms")

  def __str__(self):
    return f"{self.room_type} {self.room_type}"

# Room metadata model
# Booking
# room id
# room cost
# room duration
# room type
# hotel id

# location model


class Rental(models.Model):
  address = map_fields.AddressField(max_length=200)
  geolocation = map_fields.GeoLocationField(max_length=100)


# Work metadata model
# Work
# work id
# work travel cost (cost to drive and return from work shift)
# expected earnings (per shift)
# number of shifts

# Budget metadata model
# budget id
# work travel cost (foreign)
# room cost (optional depending on situation) (foreign)
# expected earnings (foreign)
# number of shifts (foreign)






