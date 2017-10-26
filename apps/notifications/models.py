from django.db import models
from users.models import UserProfile
from common.models import Family
from chores.models import Chore
from finances.models import Charge
from events.models import Event

class Notification(models.Model):
    notify = models.ManyToManyField(UserProfile,related_name="notify")
    app = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
    link = models.CharField(max_length=40)
    read_by = models.ManyToManyField(UserProfile,blank=True)
    time = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
	comment = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	commented_by = models.ForeignKey(UserProfile)
	likes = models.IntegerField()

class AppEvent(models.Model):
	chore = models.ForeignKey(Chore)
	charge = models.ForeignKey(Charge)
	event = models.ForeignKey(Event)

class Post(models.Model):
	family = models.ManyToManyField(Family)
	message = models.CharField(max_length=200)
	date_created = models.DateTimeField(auto_now_add=True)
	posted_by = models.ForeignKey(UserProfile)
	likes = models.IntegerField(null=True,blank=True)
	comments = models.ManyToManyField(Comment)
	app_event = models.OneToOneField(AppEvent,null=True)