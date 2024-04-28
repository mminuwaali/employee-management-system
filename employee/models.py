from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    date_joined = models.DateField()
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    user = models.OneToOneField(User, models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.department} - {self.position}"


class Attendance(models.Model):
    check_out = models.DateTimeField(auto_now=True)
    check_in = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(Employee, models.CASCADE)


class Leave(models.Model):
    end_date = models.DateField()
    start_date = models.DateField()
    description = models.TextField(default="")
    status = models.BooleanField(null=True, blank=True)
    employee = models.ForeignKey(Employee, models.CASCADE)


class PerformanceEvaluation(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)
