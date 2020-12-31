from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHER = 'other'

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
        (GENDER_OTHER, 'Other')
    )

    LANGUAGE_ENGLISH = 'en'
    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, 'English'),
    )

    AMERICAN_DOLLARS = 'usd'
    INDIAN_RUPEES = 'inr'

    CURRENCY_CHOICES = (
        (AMERICAN_DOLLARS, 'USD'),
        (INDIAN_RUPEES, 'INR')
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2, default=LANGUAGE_ENGLISH)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=2, default=AMERICAN_DOLLARS)
    superhost = models.BooleanField(default=False)
    


