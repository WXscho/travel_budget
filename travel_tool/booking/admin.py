from django.contrib import admin

# Register your models here.

from .models import Hotel

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
admin.site.register(Hotel, HotelAdmin)