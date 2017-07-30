from django.core.management.base import BaseCommand
from common.models import Institution
import csv
import os


class Command(BaseCommand):
    help = 'Seeds universities for the site'

    def handle(self, *args, **options):
        institutions_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Institutions.csv')
        with open(institutions_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                institution_id = row['Institution_ID']
                name = row['Institution_Name']
                zip_code = row['Institution_Zip']
                website = row['Institution_Web_Address']
                campus_name = row['Campus_Name']
                campus_zip = row['Campus_Zip']
                Institution.objects.get_or_create(institution_id = institution_id, name = name,zip_code = zip_code, website=website,
                    campus_name = campus_name,campus_zip = campus_zip)
            print("Done!")
