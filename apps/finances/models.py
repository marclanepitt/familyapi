from django.db import models


class Charge(models.Model):
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
