from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=50)
    pro_pic = models.ImageField(blank=True, null=True)
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
