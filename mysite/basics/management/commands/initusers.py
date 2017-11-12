from django.core.management.base import BaseCommand

from basics.fake_data import populate_users


class Command(BaseCommand):
    help = 'Creates basic users for the application'

    def handle(self, *args, **options):
        populate_users(self)
