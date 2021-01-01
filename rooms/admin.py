from django.contrib import admin
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        ("Basic Info", {
            "fields": (
              'name',
              'description',
              'address',
              'price'  
            ),
        }),
        ("Time", {
            "fields": (
              'check_in',
              'check_out',
              'instant_book'
            ),
        }),
        ("Spaces", {
            "fields": (
              'guests', 
              'beds', 
              'bedrooms',
              'baths' 
            ),
        }),
        ("More about Spaces", {
            "classes": ('collapse',),
            "fields": (
              'amenities',
              'facilities',
              'house_rules'
            ),
        }),
         ("Last Details", {
            "fields": (
              'host',  
            ),
        })
    )
    
    list_display = [
        'name',
        'country',
        'city',
        'price',
        'guests',
        'beds',
        'bedrooms',
        'baths',
        'check_in',
        'check_out',
        'instant_book'
    ]

    list_filter = ['instant_book', 'city', 'country']

    search_fields = ('=city', '^host__username')

    filter_horizontal = ('amenities', 'facilities', 'house_rules')
 
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
