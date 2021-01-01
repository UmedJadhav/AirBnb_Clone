from django.contrib import admin
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass

 
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
