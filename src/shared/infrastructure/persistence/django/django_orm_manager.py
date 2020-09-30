from django.db.models import Model


class DjangoOrmManager:
    model = Model

    def django_read(self, **fields):
        try:
            return self.model.objects.get(**fields)
        except Exception as err:
            return None

    def django_create(self, **fields):
        model_instance = self.model()
        for field, value in fields.items():
            if hasattr(model_instance, field):
                setattr(model_instance, field, value)
            else:
                raise Exception('Field not found')
        try:
            model_instance.save()
        except Exception as err:
            # Log this error
            raise Exception(f'Error when try to save {self.model}')

    def django_all(self):
        return self.model.objects.all()
