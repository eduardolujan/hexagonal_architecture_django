

# -*- coding: utf-8 -*-

import os
import traceback

import environ
from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command

USER_FIXTURES = {
    'app': {
        'develop': [
            'address.json',
            'phone.json',
            'person.json'
        ]
    }
}


class Command(BaseCommand):
    """
    Command for load person
    """

    help = 'Load all fixtures of {app}'.format(app='Users')

    def add_arguments(self, parser):
        parser.add_argument('-a', '--application',
                            type=str,
                            help='Define application to create')
        parser.add_argument('-e', '--enviroment',
                            type=str,
                            help='Define enviroment to user')

    def get_path(self):
        app_path = environ.Path(__file__) - 3
        fixtures_path = os.path.join(str(app_path), 'fixtures')
        if not os.path.exists(fixtures_path):
            raise Exception('Folder de fixtures no existe')
        return fixtures_path

    def handle(self, *args, **options):
        application = options.get('application')
        enviroment = options.get('enviroment')
        fixtures_path = self.get_path()

        if not application:
            raise CommandError(f'Application param is empty')

        if not enviroment:
            raise CommandError(f'Environment param is empty')

        fixtures = USER_FIXTURES.get(application, {}).get(enviroment, [])
        if not fixtures:
            raise CommandError(f'Not fixtures detected: {fixtures}')

        for fixture in fixtures:
            try:
                initial_msg = f'Running {fixture} fixture'
                self.stdout.write(self.style.SUCCESS(initial_msg))
                fixture_path = f'persons/{enviroment}/{fixture}'
                fixture_path = os.path.join(fixtures_path, fixture_path)
                print(fixtures_path)
                if os.path.exists(fixture_path):
                    call_command('loaddata', fixture_path)

                else:
                    error_msg = f'El fixture {fixture_path} no existe verifica'
                    self.stdout.write(self.style.ERROR(error_msg))

            except Exception as err:
                print(f'Error in {__name__} fixture {fixture}, err:{err}')
                traceback.print_exc()
                raise CommandError('Message {}'.format(err))
