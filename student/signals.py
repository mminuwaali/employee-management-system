from . import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=models.Enrollment)
def create_user_upon_successful_enrollment(sender, instance, created, *args, **kwargs):
    if not created and instance.status == True:
        password = User.objects.make_random_password()
        User.objects.create_user(**instance)
