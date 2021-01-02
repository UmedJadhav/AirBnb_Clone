from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):
    help = 'This command populates the db with fake user data'

    def add_arguments(self, parser):
        parser.add_argument('--number', default=1, type=int,  help='How many users are to be created')

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        number = options.get('number', 1)
        seeder.add_entity(User, number, {
            'is_staff': False,
            'is_superuser': False,
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Users Created !"))
