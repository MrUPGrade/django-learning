from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from random import randint

from . import models as m


from django.conf import settings

FAKE_DATA_DIR = settings.BASE_DIR / '..' / 'fake_data'


class DBPopulateHelper:
    def __init__(self, cmd):
        self._cmd = cmd

    def _print_user(self, user):
        self._cmd.stdout.write(
            self._cmd.style.SUCCESS('Successfully create user "%s" with id "%s"' % (user.username, user.id)))

    def create_user_if_not_exist(self, username, email, password, is_admin=False):
        try:
            user = User.objects.filter(username__exact=username).get()
        except ObjectDoesNotExist as e:
            if is_admin:
                user = User.objects.create_superuser(username, email, password)
            else:
                user = User.objects.create_user(username, email, password)
            user.save()
            self._print_user(user)

        return user


def populate_users(cmd):
    db = DBPopulateHelper(cmd)
    users = [
        db.create_user_if_not_exist('admin', 'admin@admin.pl', 'admin', is_admin=True),
        db.create_user_if_not_exist('user', 'user@admin.pl', 'user'),
        db.create_user_if_not_exist('newuser', 'newuser@admin.pl', 'newuser'),
        db.create_user_if_not_exist('datauser', 'newuser@admin.pl', 'datauser'),
    ]

    return users


def populate_contacs_and_tags(cmd):
    users = populate_users(cmd)
    user = users[1]
    data_user = users[3]

    FAKE_TAGS = 100
    FAKE_CONTACTS = 100

    tag1 = m.Tag.objects.create(name='Praca')
    tag2 = m.Tag.objects.create(name='Dom')
    tag3 = m.Tag.objects.create(name='Rodzina')

    tag_list = []

    for x in range(0, FAKE_TAGS):
        t = m.Tag.objects.create(name='tag%s' % x)
        tag_list.append(t)

    c1 = m.Contact.objects.create(first_name='Jan', last_name='Kowalski', email='jk@gmail.com', phone='123456789',
                                  user=user)
    c1.tags.add(tag1)
    c1.tags.add(tag2)
    c1.tags.add(tag3)
    c1.save()

    with (FAKE_DATA_DIR / 'profile.png').open('rb') as f:
        c1.profile_pic.save('file1', f)

    c1.save()

    c2 = m.Contact.objects.create(first_name='Janusz', last_name='Iksinski', user=user)
    c2.tags.add(tag1)

    for x in range(0, FAKE_CONTACTS):
        contact_data = {
            'first_name': 'First%s' % (x,),
            'last_name': 'last%s' % (x,),
            'user': data_user
        }
        c = m.Contact.objects.create(**contact_data)
        for x in range(0, randint(0, 10)):
            random_tag = tag_list[randint(0, FAKE_TAGS-1)]
            c.tags.add(random_tag)

        c.save()
