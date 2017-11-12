from django.core.management.base import BaseCommand

from basics.fake_data import populate_contacs_and_tags


class Command(BaseCommand):
    help = 'Creates basic data for the application'

    def handle(self, *args, **options):
        populate_contacs_and_tags(self)
