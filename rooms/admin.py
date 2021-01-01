from django.contrib import admin
from .models import Room, RoomType, Facility, Amenity, HouseRule, Photo


@admin.register(RoomType, Facility, Amenity, HouseRule)
class ItemAdmin(admin.ModelAdmin):

    list_display = [
        'name',
        'used_by'
    ]
    
    def used_by(self, curr_row):
        return curr_row.rooms.count()


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
        'ratings_avg'

    ]

    list_filter = ['instant_book', 'city', 'country']

    search_fields = ('=city', '^host__username')

    filter_horizontal = ('amenities', 'facilities', 'house_rules')

    def count_amenities(self,  curr_row):
        return curr_row.amenities.count()

    count_amenities.short_description = 'No. amenities'

    def count_photos(self, curr_row):
        return curr_row.photos.count()
    
    def ratings_avg(self):
        reviews =  self.reviews.all()
        total_avg = 0
        for review in reviews:
            total_avg += review.rating_avg()
        return round(total_avg / len(reviews),2)
    

 
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass
