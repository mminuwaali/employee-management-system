from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

GENDER = [(i, i) for i in ["Male", "Female", "Other"]]

MARITAL_STATUS = [(i, i) for i in ["Other", "Single", "Married", "Divorced", "Widowed"]]


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    address = models.TextField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    nationality = models.CharField(max_length=50, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    emergency_contact = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, null=True, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", null=True, blank=True)
    marital_status = models.CharField(
        max_length=10, choices=MARITAL_STATUS, null=True, blank=True
    )

    @property
    def gender_choice(self):
        return [i[0] for i in GENDER]

    @property
    def marital_status_choice(self):
        return [i[0] for i in MARITAL_STATUS]

    def __str__(self):
        return self.user.username


class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.email}"
