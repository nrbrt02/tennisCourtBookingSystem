from django.contrib import admin

from App.models import Booking, Court, Image, Sessions

# Register your models here.

admin.site.register(Court)
admin.site.register(Image)
admin.site.register(Sessions)
admin.site.register(Booking)