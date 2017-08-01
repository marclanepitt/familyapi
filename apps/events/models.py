from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    event_pic = models.ImageField(blank=True, null=True)
    date = models.DateTimeField()
    # participants
