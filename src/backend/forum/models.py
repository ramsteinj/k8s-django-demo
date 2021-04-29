import logging
from django.db import models
from users.models import YogiyoUser

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Parent model
class Forum(models.Model):
    user_id = models.ForeignKey(YogiyoUser, on_delete=models.CASCADE, db_column='user_id') 
    forum_id = models.AutoField(primary_key=True, db_column='forum_id')
    topic = models.CharField(max_length=300)
    description = models.CharField(max_length=1000, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.user_id, self.forum_id, self.topic)

    class Meta:
        ordering = ['created']
 
# Child model
class Discussion(models.Model):
    user_id = models.ForeignKey(YogiyoUser, on_delete=models.CASCADE, db_column='user_id')
    forum_id = models.ForeignKey(Forum, blank=True, on_delete=models.CASCADE, db_column='forum_id')
    discussion_id = models.AutoField(primary_key=True, db_column='discussion_id')
    discuss = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return str(self.user_id, self.forum_id, self.discussion_id, self.discuss)

    class Meta:
        ordering = ['created']
