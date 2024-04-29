from . import models
from django.db.models import Q
from django.dispatch import receiver
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=models.Enrollment)
def create_user_upon_successful_enrollment(sender, instance, created, *args, **kwargs):
    if (
        not created  # if it's an update
        and instance.status == True  # if the enrollment is approved
        and not User.objects.filter(
            Q(email=instance.email) | Q(username=instance.username)
        ).exists()
    ):
        password = User.objects.make_random_password()
        user = User.objects.create_user(
            password=password,
            email=instance.email,
            username=instance.username,
            last_name=instance.last_name,
            first_name=instance.first_name,
        )

        user.groups.add(Group.objects.get_or_create(name="student")[0])
        models.Student.objects.create(user=user, department=instance.department)

        print(password)
