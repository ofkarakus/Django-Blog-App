from django.db.models.signals import post_save  # will be executed
from django.contrib.auth.models import User  # will send signal
from django.dispatch import receiver  # will receive signal
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
