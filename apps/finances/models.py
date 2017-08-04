from django.db import models
from common.models import Family
from users.models import UserProfile


class Charge(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    FOOD = 'FO'
    CLOTHING = 'CL'
    ENTERTAINMENT = 'EN'
    OTHER = "O"

    CHARGE_CHOICES = (
        (FOOD, "Food"),
        (CLOTHING, "Clothing"),
        (ENTERTAINMENT, "Entertainment"),
        (OTHER, "Other"),
    )
    charge_type = models.CharField(
        max_length=2,
        choices=CHARGE_CHOICES,
        default=OTHER,
    )

    amount = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(max_length=50)

    def __str__(self):
        return '{} spent ${} at {}'.format(self.created_by, self.amount, self.location)
