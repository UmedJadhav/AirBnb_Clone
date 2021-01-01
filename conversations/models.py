from django.db import models
from core.models import Time_stamped_Model


class Message(Time_stamped_Model):
    message = models.TextField()
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    conversation = models.ForeignKey('Conversation', related_name='messages', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} says {self.message}"


# Create your models here.
class Conversation(Time_stamped_Model):
    participants = models.ManyToManyField('users.User', blank=True)
    
    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username) 
        return str(' - '.join(usernames))
    
    def count_messages(self):
        return self.messages.count()  # I can access message here since message has a foreign key
    
    count_messages.short_description = 'no. messages'

    def count_participants(self):
        return self.participants.count()  # I can access message here since message has a foreign key
    
    count_messages.short_description = 'no. participants'
