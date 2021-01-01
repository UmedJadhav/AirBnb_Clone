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
    file = models.ImageField()
    room = models.ForeignKey(to="Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption 


# Create your models here.
class Room(Time_stamped_Model):
    name = models.CharField(max_length=140)
    host = models.ForeignKey(to=User, on_delete=models.CASCADE)  # What to do when User gets deleted
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=200)
    beds = models.IntegerField()
    baths = models.IntegerField() 
    guests = models.IntegerField()
    check_in = models.TimeField()  # From 0 - 24 hrs
    checkout_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)


    def __str__(self):
        return self.name

