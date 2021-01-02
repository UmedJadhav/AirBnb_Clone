import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django_seed import Seed
from reservations.models import Reservation
from users.models import User  
from rooms.models import Room  


class Command(BaseCommand):
    help = 'This command populates the db with fake Reservations data'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int,  help='How many reservations are to be created')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get('number', 1)
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(Reservation, number, {
            'status': lambda x: random.choice(['pending', 'confirmed','cancelled']),
            'guest': lambda x: random.choice(users),
            'room': lambda x: random.choice(rooms),
            'check_in': lambda x: datetime.now(),
            'check_out': lambda x: datetime.now() + timedelta(days=random.randint(3, 15))
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Reservations Created !"))
