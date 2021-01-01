from django.db import models
from core.models import Time_stamped_Model


# Create your models here.
class Review(Time_stamped_Model):
    review = models.TextField()
    accuracy = models.IntegerField()
    communication = models.IntegerField()
    cleanliness = models.IntegerField()
    location = models.IntegerField()
    check_in = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.review} - {self.room}'