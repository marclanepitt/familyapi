from django.core.management.base import BaseCommand
from common.models import Major
import csv
import os

class Command(BaseCommand):
	help = 'Seeds majors for the site'
	def handle(self, *args, **options):
		majors_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Majors.csv')
		with open(majors_file) as csvfile:
			reader = csv.DictReader(csvfile)
			for row in reader:
				major = row['Major']
				category=row['Major_Category']
				new_major = Major.objects.get_or_create(major=major,category=category)
			print("Majors Done!")
