from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):
    help = 'This command populates the db with fake facility data'

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]
        for facility  in facilities:
            Facility.objects.create(name=facility)
        self.stdout.write(self.style.SUCCESS("Facilities Created !"))
    