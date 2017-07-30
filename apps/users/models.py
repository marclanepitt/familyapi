from django.db import models

from django.contrib.auth.models import User
from common.models import Family


class Guardian(models.Model):
    MOTHER = 'M'
    FATHER = 'F'
    AUNT = 'A'
    UNCLE = 'U'
    GRANDFATHER = "GF"
    GRANDMOTHER = "GM"

    GUARDIAN_STATUS_CHOICES = (
        (MOTHER, 'Mother'),
        (FATHER, 'Father'),
        (AUNT, "Aunt"),
        (UNCLE, 'Uncle'),
        (GRANDMOTHER, 'Grandmother'),
        (GRANDFATHER, 'Grandfather')
    )
    status = models.CharField(
        max_length=2,
        choices=GUARDIAN_STATUS_CHOICES,
        default=MOTHER,
    )


class Child(models.Model):
    SON = 'S'
    DAUGHTER = 'D'
    NIECE = 'NC'
    NEPHEW = 'NP'
    GRANDSON = 'GS'
    GRANDDAUGHTER = 'GD'


    CHILD_STATUS_CHOICES = (
        (SON, 'Son'),
        (DAUGHTER, 'Daughter'),
        (NIECE, "Niece"),
        (NEPHEW, 'Nephew'),
        (GRANDSON, 'Grandson'),
        (GRANDDAUGHTER, 'Granddaughter')
    )
    status = models.CharField(
        max_length=2,
        choices=CHILD_STATUS_CHOICES,
        default=SON,
    )



class UserProfile(models.Model):
    guardian = models.OneToOneField(Guardian, null = True)
    child = models.OneToOneField(Child, null = True)
    date_of_birth = models.DateField(auto_now = False, default = "1997-07-28")
    user = models.OneToOneField(User)
    pro_pic = models.ImageField(blank = True)
    family = models.ForeignKey(Family, on_delete = models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

