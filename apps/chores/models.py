from django.db import models
from users.models import UserProfile
from common.models import Pet,Family


class Chore(models.Model):
    family = models.ForeignKey(Family)
    created_by = models.ForeignKey(UserProfile)
    name = models.CharField(max_length=100)

    days = models.CharField(max_length=10)
    time_start = models.TimeField()
    time_end = models.TimeField()
    date_start = models.DateField()
    is_completed = models.BooleanField(default=False)
    completed_date = models.DateTimeField(blank=True,null=True)
    is_redeemed =models.BooleanField(default=False)
    redeemed_date = models.DateTimeField(blank=True,null=True)
    num_points = models.IntegerField()

    WEEKLY = 'WE'
    BIWEEKLY = "BW"
    TRIWEEKLY = "TW"
    MONTHLY = "MO"
    NEVER = "N"

    interval_choices = (
        (NEVER,"Never"),
        (WEEKLY, "Weekly"),
        (BIWEEKLY, "Bi Weekly"),
        (MONTHLY, "Monthly"),
        (TRIWEEKLY, "Tri Weekly")
    )

    repeat = models.CharField(max_length=2, choices=interval_choices, default=WEEKLY)
    participants = models.ManyToManyField(UserProfile, related_name="participants",blank=True)
    pets = models.ManyToManyField(Pet,blank=True)
    is_latest = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.name)

class ChoreReward(models.Model):
    created_by = models.ForeignKey(UserProfile, related_name='created_by')
    rewarded_to = models.ForeignKey(UserProfile, related_name="rewarded_to")
    num_points = models.IntegerField()
    reward = models.CharField(max_length=100)


#parents will set chore point thresholds with a reward at each
#this will be on userprofile model, when threshold is reached, points can be redeemed
#should add is_completed field to this model
#eventually add in link to chore reward or image
#chore open to anyone vs chore to specific person
#what happens when chores are past due?