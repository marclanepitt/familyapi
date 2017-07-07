from django.db import models

class Institution(models.Model):
    institution_id = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    zip_code = models.CharField(max_length=10)
    website = models.CharField(max_length=50)
    campus_name = models.CharField(max_length=30)
    campus_zip = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Major(models.Model):
    major = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    def __str__(self):
        return self.major
