from django.db import models
from django import forms
from common.models import Family


class UserProfile(models.Model):
    password = models.CharField(max_length=4)
    first_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(auto_now=False)
    pro_pic = models.ImageField(blank=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, blank=True, null=True,related_name="users")
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    chore_points = models.IntegerField()

    DAILY ="Day"
    WEEKLY= 'Week'
    MONTHLY="Month"
    YEARLY = "Year"

    interval_choices = (
        (DAILY, "Daily"),
        (WEEKLY,"Weekly"),
        (MONTHLY,"Monthly"),
        (YEARLY,"Yearly")
    )

    budget_interval = models.CharField(max_length=5,choices=interval_choices,default=WEEKLY)

    SUPER = 'SU'
    ADMIN = 'AD'
    DEFAULT = "DE"

    admin_choices = (
        (SUPER, "Super"),
        (ADMIN, "Admin"),
        (DEFAULT,"Default")
    )

    admin = models.CharField(
        max_length=2,
        choices=admin_choices,
        default=DEFAULT,
    )

    MOTHER = 'M'
    FATHER = 'F'
    AUNT = 'A'
    UNCLE = 'U'
    GRANDFATHER = "GF"
    GRANDMOTHER = "GM"
    SON = 'S'
    DAUGHTER = 'D'
    NIECE = 'NC'
    NEPHEW = 'NP'
    GRANDSON = 'GS'
    GRANDDAUGHTER = 'GD'

    STATUS_CHOICES = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (AUNT, "Aunt"),
        (UNCLE, 'Uncle'),
        (GRANDMOTHER, 'Grandmother'),
        (GRANDFATHER, 'Grandfather'),
        (SON, 'Son'),
        (DAUGHTER, 'Daughter'),
        (NIECE, "Niece"),
        (NEPHEW, 'Nephew'),
        (GRANDSON, 'Grandson'),
        (GRANDDAUGHTER, 'Granddaughter')
    )

    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default=MOTHER,
    )

    def __str__(self):
        return '{} {}'.format(self.first_name, self.family.name)

