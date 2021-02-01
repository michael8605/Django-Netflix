from django.db import models
from django.utils import timezone

# Create your models here.
class Movies(models.Model):
    # parent_tweet_id = models.SmallIntegerField( null = True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=225)
    description = models.CharField(max_length=1000)
    category_id = models.CharField(max_length=100)
    image_path = models.CharField(max_length=225)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name