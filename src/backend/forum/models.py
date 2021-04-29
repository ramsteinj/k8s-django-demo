import logging
from django.db import models
from users.models import YogiyoUser

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Parent model
class Forum(models.Model):
    userid = models.ForeignKey(YogiyoUser, on_delete=models.CASCADE)
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.topic)

    class Meta:
        ordering = ['created']
 
# Child model
class Discussion(models.Model):
    userid = models.ForeignKey(YogiyoUser, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.forum)

    class Meta:
        ordering = ['created']
