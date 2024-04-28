from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GENDER = [("M", "Male"), ("F", "Female"), ("O", "Other")]

MARITAL_STATUS = [
    ("O", "Other"),
    ("S", "Single"),
    ("M", "Married"),
    ("D", "Divorced"),
    ("W", "Widowed"),
]


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)
    marital_status = models.CharField(max_length=1, choices=MARITAL_STATUS, null=True, blank=True)

    def __str__(self):
        return self.user.username
