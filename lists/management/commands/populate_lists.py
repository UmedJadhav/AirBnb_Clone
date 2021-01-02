import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from lists.models import List
from users.models import User  
from rooms.models import Room  


class Command(BaseCommand):
    help = 'This command populates the db with fake Lists data'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int,  help='How many lists are to be created')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get('number', 1)
        users = User.objects.all()
        rooms = Room.objects.all()
        seeder.add_entity(List, number, {
            'user': lambda x: random.choice(users),
        })
        created = seeder.execute()
        cleaned = flatten(list(created.values()))
        for pk in cleaned:
            list_model = List.objects.get(pk=pk)
            to_add = rooms[random.randint(1, 5): random.randint(6, 30)]
            list_model.rooms.add(*to_add)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Listings Created !"))
