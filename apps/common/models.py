from django.db import models
from django.contrib.auth.models import User

class Family(models.Model):
    name = models.CharField(max_length=50)
    pro_pic = models.ImageField(blank=True, null=True)
    cover_pic = models.ImageField(blank=True,null=True)
    user = models.OneToOneField(User)
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length=50)
    pro_pic = models.ImageField(blank=True, null=True)
    DOG = "DO"
    CAT = "CA"

    PET_CHOICES = (
        (DOG, "dog"),
        (CAT, "cat"),
    )

    pet_choice = models.CharField(
        max_length=2,
        choices=PET_CHOICES,
        default=DOG,
    )

    date_of_birth = models.DateField(auto_now=False, blank=True, null=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=50)
    pro_pic = models.ImageField(blank=True, null=True)
    families = models.ManyToManyField(Family)
    def __str__(self):
        return self.name

class Post(models.Model):
    family = models.ForeignKey(Family)
    date = models.DateTimeField(auto_now_add=True)

# class Notification(models.Model):
#     notify = models.ManyToManyField(UserProfile)
#     app = models.CharField(max_length=20)
#     message = models.CharField(max_length=100)
#     link = models.CharField(max_length=40)