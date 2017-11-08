from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates basic users for the application'

    def _print_user(self, user):
        self.stdout.write(self.style.SUCCESS('Successfully create user "%s" with id "%s"' % (user.username, user.id)))

    def handle(self, *args, **options):
        try:
            admin = User.objects.filter(username__exact='admin').get()
        except ObjectDoesNotExist as e:
            admin = User.objects.create_superuser('admin', 'admin@fakedomain.pl', 'admin')
            admin.save()
            self._print_user(admin)

        try:
            user = User.objects.filter(username__exact='user').get()
        except ObjectDoesNotExist as e:
            user = User.objects.create_user('user', 'user@fakedomain.pl', 'user')
            user.save()
            self._print_user(user)
