from django.contrib import admin

# Register your models here.

from .models import Hotel, Room

class HotelAdmin(admin.ModelAdmin):
  list_display = (
        "hotel_name",
        "hotel_address",
        "hotel_city",
        "hotel_state",
        "hotel_zip",
        "hotel_rated",
    )

  # limiting what fields are shown to admin
  fields = (
    "hotel_name",
    "hotel_address",
    "hotel_city",
    "hotel_state",
    "hotel_zip",
    "hotel_rated",
  )
class RoomAdmin(admin.ModelAdmin):
  list_display = (
        "room_id",
        "room_type",
        "room_duration",
        "room_cost",
        "hotel",
    )

admin.site.register(Hotel, HotelAdmin)
admin.site.register(Room, RoomAdmin)