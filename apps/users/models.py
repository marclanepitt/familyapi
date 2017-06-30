from django.db import models
from common.models import Institution,Major
from django.contrib.auth.models import User


class UserProfile(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRAD = 'GR'
    FACULTY = 'FC'

    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRAD, 'Graduate Student'),
        (FACULTY, 'Faculty')
    )
    year = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    institution = models.ForeignKey(Institution)
    major = models.ForeignKey(Major)
    user = models.OneToOneField(User)

    def __str__(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
