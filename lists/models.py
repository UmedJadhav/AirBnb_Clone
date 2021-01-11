from django.db import models
from core.models import Time_stamped_Model


# Create your models here.
class List(Time_stamped_Model):
    name = models.CharField(max_length=80)
    user = models.OneToOneField(to='users.User', on_delete=models.CASCADE)
    rooms = models.ManyToManyField(to='rooms.Room', blank=True)

    def __str__(self):
        return self.name

    def count_rooms(self):
        return self.rooms.count()
    
    count_rooms.short_description = 'no. rooms'
