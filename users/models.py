  
import uuid
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.shortcuts import reverse
from django.template.loader import render_to_string
from core import managers as core_managers


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

    LOGIN_EMAIL = "email"
    LOGIN_GITHUB = "github"

    LOGIN_CHOICES = (
        (LOGIN_EMAIL, "Email"),
        (LOGIN_GITHUB, "Github")
    )

    bio = models.TextField(default="", blank=True)
    avatar = models.ImageField( blank=True, upload_to='avatars')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2,
                                default=LANGUAGE_ENGLISH, blank=True)
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3,
                                default=AMERICAN_DOLLARS, blank=True)
    superhost = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)
    login_method = models.CharField(
        max_length=50, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    objects = core_managers.CustomUserManager()

    def get_absolute_url(self):
        return reverse("users:profile", kwargs={"pk": self.pk})

    def verify_email(self):
        if self.email_verified is False:
            secret = uuid.uuid4().hex[:20]
            self.email_secret = secret
            html_message = render_to_string(
                "emails/verify_email.html", {"secret": secret}
            )
            send_mail(
                _("Verify Airbnb Account"),
                strip_tags(html_message),
                settings.EMAIL_FROM,
                [self.email],
                fail_silently=True,
                html_message=html_message,
            )
            self.save()
        return
