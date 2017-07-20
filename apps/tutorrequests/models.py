from django.db import models

# Create your models here.

class Cram(models.Model):
	dateStart = models.DateTimeField(null=True)
	dateEnd = models.DateTimeField(null=True)
	multiplier = models.DecimalField(max_digits = 4, decimal_places = 3)
	location = models.CharField(max_length = 100, null = True)


class TutorRequest(models.Model):
	# student_id = models.CharField(max_length=20)
	# tutor_id = models.CharField(max_length=20,null = True)

	student = models.ForeignKey('auth.User', related_name='tutor_request')
	tutor  = models.ForeignKey('auth.User', related_name='tutor_reqest')

	cancelled = models.NullBooleanField()
	student_accept = models.NullBooleanField()
	tutor_accept = models.NullBooleanField()
	
	#Student/Tutor must mutually agree to cancel a session w/o pay
	student_cancel = models.NullBooleanField() 
	tutor_cancel = models.NullBooleanField()

	answer_date = models.DateTimeField(null=True)
	building = models.CharField(max_length = 100)
	location = models.CharField(max_length = 100)
	help_description = models.CharField(max_length = 300)
	subject = models.CharField(max_length = 50)
	type_help = models.CharField(max_length = 50)
	dateTime = models.DateTimeField(null=True)
	timeElapsed = models.DateTimeField(null=True)
	cram = models.ForeignKey(Cram, null = True)
	amount = models.DecimalField(max_digits = 11, decimal_places = 10, default = 0)




