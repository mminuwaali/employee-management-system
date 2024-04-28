from . import models
from django.dispatch import receiver
from django.db.models.signals import post_save


@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, *args, **kwargs):
    if created and not (instance.is_staff or instance.is_superuser):
        return models.Profile.objects.create(user=instance)
