import inspect
import django
from django.db.models.fields.related_descriptors import ForwardOneToOneDescriptor, ForwardManyToOneDescriptor
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from had.app.models import Person, Address


members = inspect.getmembers(Person, lambda a: not inspect.isroutine(a))
members_dict = dict(members)
address = members_dict.get('address')
if type(address) is ForwardManyToOneDescriptor:
    pass
    print(f"{address}")
pass



class DetectForeignKey:
    def __init__(self):
        pass


