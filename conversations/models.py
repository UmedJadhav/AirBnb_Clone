from django.db import models
from core.models import Time_stamped_Model


class Message(Time_stamped_Model):
    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says {self.message}"


# Create your models here.
class Conversation(Time_stamped_Model):
    participants = models.ManyToManyField('users.User', blank=True)
    
    def __str__(self):
        return str(self.created)
    
