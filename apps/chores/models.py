from django.db import models

class Chore(models.Model):
	name = models.CharField(max_length=20)
	
