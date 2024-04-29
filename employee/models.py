import locale
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model

User = get_user_model()


class Employee(models.Model):
    date_joined = models.DateField(default=now)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.OneToOneField(
        User, models.CASCADE, limit_choices_to={"groups__name": "employee"}
    )

    @property
    def salary_value(self):
        locale.setlocale(locale.LC_ALL, "en_NG.UTF-8")
        return locale.currency(self.salary, grouping=True)

    class Meta:
        ordering = ["-date_joined"]

    def __str__(self):
        return f"{self.user.username} - {self.department} - {self.position}"


class Attendance(models.Model):
    check_out = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    check_in = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(
        Employee, models.CASCADE, limit_choices_to={"user__groups__name": "employee"}
    )

    @property
    def has_ended(self):
        print(self.check_in.second, self.check_out.second, self.check_in.second != self.check_out.second)
        return self.check_in.second != self.check_out.second

    class Meta:
        ordering = ["-created_at"]


class Leave(models.Model):
    end_date = models.DateField()
    start_date = models.DateField()
    reason = models.TextField(default="")
    description = models.TextField(default="")
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    employee = models.ForeignKey(
        Employee, models.CASCADE, limit_choices_to={"user__groups__name": "employee"}
    )

    @property
    def status_string(self):
        if self.status == None:
            return "Undecided"
        return "Accepted" if self.status else "Rejected"

    class Meta:
        ordering = ["-created_at"]


# class PerformanceEvaluation(models.Model):
#     employee = models.ForeignKey(Employee, models.CASCADE)
