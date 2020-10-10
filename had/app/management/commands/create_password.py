# -*- coding: utf-8 -*-


from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.hashers import make_password


class Command(BaseCommand):

    help = 'Create user password'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--password',
                            type=str,
                            help='User password')

    def handle(self, *args, **options):
        password = options.get('password')
        if not password:
            raise CommandError('Error password is empty')
        hashed_password = make_password(password)
        self.stdout.write(self.style.ERROR(f'Hashed password: {hashed_password}'))
