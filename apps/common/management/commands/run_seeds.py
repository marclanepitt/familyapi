from django.contrib.sites.models import Site
from django.core.management.base import BaseCommand


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
