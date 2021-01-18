from django.db import models
from django.contrib.auth.models import User


def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to=user_profile_path, default='user.png')

    def __str__(self):
        return str(self.user)
