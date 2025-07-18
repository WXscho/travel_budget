from django.db import models

# Create your models here.

#

# Hotel metadata model
class Hotel(models.Model):
  hotel_id = models.AutoField(primary_key=True)
  hotel_name = models.CharField(max_length=100)
  hotel_address = models.CharField(max_length=100)
  hotel_city = models.CharField(max_length=100)
  hotel_state = models.CharField(max_length=100)
  hotel_zip = models.CharField(max_length=100)
  hotel_rated= models.DecimalField(decimal_places=1,
                                   max_digits=2,
                                   choices=[(x/2, f"{x/2}") for x in range(2,11)]
                                   )
  def __str__(self):
    return f"{self.hotel_name} {self.hotel_rated} Stars"
# Hotel
# hotel id
# hotel name
# hotel address
# hotel rating

# Room metadata model
# Booking
# room id
# room cost per day
# room duration
# room type
# hotel id

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






