from django.core.management.base import BaseCommand
from chores.models import Chore
import time,datetime


class Command(BaseCommand):
    help = 'Creates chores when expiring'

    def handle(self, *args, **options):
      cs = Chore.objects.filter(is_latest = True, date_start=time.strftime("%Y-%m-%d"))
      for chore in cs:
          chore.pk = None
          chore.is_redeemed=False
          chore.is_completed=False
          if(chore.repeat == 'WE'):
              i = 1
              while i < 6:
                chore.date_start = chore.date_start + datetime.timedelta(days=7)
                chore.save()
                i = i+1
          elif(chore.repeat == 'MO'):
              pass
          elif(chore.repeat == "BW"):
              pass
          elif(chore.repeat == "TW"):
              pass
          else:
              pass