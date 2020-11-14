import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from had.app.models import Person


if __name__ == '__main__':
    pass
