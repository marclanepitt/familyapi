from django.db import models
from users.models import UserProfile
from common.models import Pet


class Chore(models.Model):
    name = models.CharField(max_length=20)
    days = models.CharField(max_length=15)
    participants = models.ManyToManyField(UserProfile)
    pets = models.ManyToManyField(Pet)
