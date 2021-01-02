from django.db import models
from django_countries.fields import CountryField
from core.models import Time_stamped_Model
from users.models import User  


class Abstract_Item(Time_stamped_Model):
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True    

    def __str__(self):
        return self.name


class RoomType(Abstract_Item):
  
    class Meta:
        verbose_name_plural = 'Room Types'


class Amenity(Abstract_Item):
    
    class Meta:
        verbose_name_plural = 'Amenities'


class Facility(Abstract_Item):
    
    class Meta:
        verbose_name_plural = 'Facilities'


class HouseRule(Abstract_Item):
    
    class Meta:
        verbose_name_plural = 'House Rules'


class Photo(Time_stamped_Model):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to='room_photos')
    room = models.ForeignKey(to="Room", related_name='photos' ,on_delete=models.CASCADE)

    def __str__(self):
        return self.caption 


# Create your models here.
class Room(Time_stamped_Model):
    name = models.CharField(max_length=140)
    host = models.ForeignKey(to=User, related_name='rooms', on_delete=models.CASCADE)  # What to do when User gets deleted
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField() 
    guests = models.IntegerField()
    check_in = models.TimeField()  # From 0 - 24 hrs
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, related_name='rooms', blank=True)
    facilities = models.ManyToManyField(Facility, related_name='rooms',blank=True)
    house_rules = models.ManyToManyField(HouseRule, related_name='rooms',blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.city = str.capitalize(self.city)
        super().save(*args, **kwargs)

    def total_rating(self):
        all_reviews = self.reviews.all()
        all_ratings = 0
        if len(all_reviews) > 0:
            for review in all_reviews:
                all_ratings += review
            return round(all_ratings/len(all_reviews), 2)
        else:
            return 0
