from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    user=[
        ('jobseeker', 'JobSeeker'),
        ('recruiter', 'Recruiter')
    ]
    user_type = models.CharField(max_length=50, blank=True, null=True, choices=user)
