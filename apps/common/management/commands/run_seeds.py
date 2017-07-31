from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Seeds the project'

    def handle(self, *args, **options):
        try:
            site = Site.objects.get(name='example.com')
            site.domain = 'family.com'
            site.name = 'family.com'
            print('Updating default site...')
            site.save()
        except Site.DoesNotExist:
            pass
