from django.contrib.auth.models import User
from django.db import models

from common.models import Family


class UserProfile(models.Model):
    date_of_birth = models.DateField(auto_now=False, default="1997-07-28")
    user = models.OneToOneField(User)
    pro_pic = models.ImageField(blank=True)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, blank=True, null=True)

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
        return '{} {}'.format(self.user.first_name, self.user.last_name)
