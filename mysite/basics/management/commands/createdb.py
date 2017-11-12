from django.db import connection

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            cursor.execute("""CREATE DATABASE mysite2""")
            cursor.execute("""GRANT ALL ON DATABASE mysite2 TO dbuser""")
