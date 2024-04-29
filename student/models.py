from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()


class Student(models.Model):
    department = models.CharField(max_length=100)
    date_enrolled = models.DateField(default=now)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.department}"


class Enrollment(models.Model):
    email = models.EmailField(unique=True)
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    status = models.BooleanField(null=True, blank=True)
    username = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=255, unique=True)


class Attendance(models.Model):
    check_out = models.DateTimeField(auto_now=True)
    check_in = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


# class Grade(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)


# class Performance(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
