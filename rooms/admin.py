from django.contrib import admin
from django.utils.html import mark_safe
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'used_by'
    ]
    
    def used_by(self, curr_row):
        return curr_row.rooms.count()


class PhotoInline(admin.TabularInline):
    model = Photo


# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    inlines = (PhotoInline, )

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
    
    ordering = [
        'name', 
        'price'
    ]

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
        'instant_book',
        'count_amenities',
        'count_photos',
        'total_rating'
    ]

    list_filter = ['instant_book', 'city', 'country']

    raw_id_fields = ( # Gives ability to filter when the host list gets long
        'host',
    )

    search_fields = (
        '=city', 
        '^host__username'
    )

    filter_horizontal = (
        'amenities', 
        'facilities', 
        'house_rules'
    )

    def count_amenities(self,  curr_row):
        return curr_row.amenities.count()

    count_amenities.short_description = 'No. amenities'

    def count_photos(self, curr_row):
        return curr_row.photos.count()

 
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        '__str__',
        'get_thumbnail'
    )

    def get_thumbnail(self, curr_row):
        return mark_safe(f'<img width=150px src={curr_row.file.url}/>')

    get_thumbnail.short_description = 'Thumbnail'
