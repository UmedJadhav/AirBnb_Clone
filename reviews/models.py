from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from core.models import Time_stamped_Model


# Create your models here.
class Review(Time_stamped_Model):
    review = models.TextField()
    accuracy = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    communication = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    cleanliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    location = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    check_in = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    value = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    user = models.ForeignKey('users.User', related_name='reviews', on_delete=models.CASCADE)
    room = models.ForeignKey('rooms.Room', related_name='reviews', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created']

    def __str__(self): 
        return f'{self.review} - {self.room}'

    def rating_avg(self):
        avg = (self.accuracy + self.communication + self.cleanliness + self.location + self.check_in + self.value ) / 6
        return round(avg, 2)