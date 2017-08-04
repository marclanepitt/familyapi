from django.db import models
from users.models import UserProfile


class Event(models.Model):
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    attendees = models.ManyToManyField(UserProfile, related_name="attendees")
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    event_pic = models.ImageField(blank=True, null=True)
    date = models.DateTimeField()
