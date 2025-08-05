from django.test import TestCase
from .models import Hotel
# Create your tests here.

class HotelModelTest(TestCase):
  def test_create_hotel(self):
    hotel = Hotel.objects.create(
      hotel_id = 1,
      hotel_name="Test Hotel",
      hotel_address = "6708 North 67th St.",
      hotel_city = 'Test City' ,
      hotel_state = 'A',
      hotel_zip = '12345',
      hotel_rated = 1
    )
    self.assertEqual(hotel.hotel_name, 'Test Hotel')
    self.assertEqual(hotel.hotel_address, '6708 North 67th St.')
    self.assertEqual(hotel.hotel_city, 'Test City')
    self.assertEqual(hotel.hotel_state, 'A')
    self.assertEqual(hotel.hotel_zip, '12345')
    self.assertEqual(hotel.hotel_rated, 1)
    self.assertIsNotNone(hotel.hotel_id)


