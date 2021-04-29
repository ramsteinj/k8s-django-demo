from django.db import models
from django.contrib.auth.models import AbstractUser

class YogiyoUser(AbstractUser):
    """
    Yogiyo user model that is extended from Abstractuser
    """
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.username
