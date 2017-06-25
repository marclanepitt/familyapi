from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeds universities for the site'

    def handle(self, *args, **options):
        pass
