import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from had.app.models import Person


from django.forms import ModelForm


class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

if __name__ == '__main__':
    data = {
        "id": "7cd0a8f0-fd2a-4ba8-979c-1facdaaad7fa",
        "name": "test",
        "last_name": "test",
        "second_last_name": "test",
        "address": "7cd0a8f0-fd2a-4ba8-979c-1facdaaad7fa",
        "phone": "7cd0a8f0-fd2a-4ba8-979c-1facdaaad7fa"
    }
    Person.objects.update_or_create()
    person_form = PersonForm(data)
    valid = person_form.is_valid()
    instance = person_form.save(commit=False)
    pass
