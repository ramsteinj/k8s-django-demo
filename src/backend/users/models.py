from django.db import models
from django.contrib.auth.models import AbstractUser

class YogiyoUser(AbstractUser):
    """
        We're going to use django's default user model with no modification.
    """

    def __str__(self):
        return self.username
