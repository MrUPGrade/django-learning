from django.conf import settings
from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    help = 'Manage users and databases'
    args = ('create', 'drop', 'recreate')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.arg_map = {
            'create': self.cmd_create,
            'drop': self.cmd_drop,
            'recreate': self.cmd_recreate
        }

    def cmd_recreate(self, ctx):
        self.cmd_drop(ctx)
        self.cmd_create(ctx)

    def cmd_drop(self, ctx):
        with connections['adm'].cursor() as cursor:
            cmd = "DROP DATABASE %s" % ctx['NAME']
            cursor.execute(cmd)

            cmd = "DROP OWNED BY %s" % ctx['USER']
            cursor.execute(cmd)

            cmd = "DROP USER %s" % ctx['USER']
            cursor.execute(cmd)

    def cmd_create(self, ctx):
        with connections['adm'].cursor() as cursor:
            cmd = "CREATE DATABASE %s" % ctx['NAME']

            cursor.execute(cmd)

            cmd = "SELECT count(*) FROM pg_roles WHERE rolname='%s'" % ctx['USER']
            cursor.execute(cmd)
            result = cursor.fetchone()
            if result[0] == 0:
                cmd = "CREATE ROLE %s WITH LOGIN PASSWORD '%s'" % (ctx['USER'], ctx['PASSWORD'])
                cursor.execute(cmd)

            cmd = "GRANT ALL ON DATABASE %s TO %s" % (ctx['NAME'], ctx['USER'])
            cursor.execute(cmd)

    def add_arguments(self, parser):
        parser.add_argument('action', choices=self.args, type=str)

    def handle(self, *args, **options):
        cmd_param = options['action']

        db_settings = settings.DATABASES['default']

        handler = self.arg_map[cmd_param]
        handler(db_settings)
