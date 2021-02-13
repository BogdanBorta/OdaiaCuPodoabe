from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(models.Model):
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(
        max_length=254, null=False, blank=False, unique=True)
    username = models.CharField(
        max_length=15, null=False, blank=False, unique=True)
    phone_number = PhoneNumberField(unique=True)
    # profile_picture = models.ImageField(upload_to='users\static\profile_pictures')

    def __str__(self):
        return self.username
