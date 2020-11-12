from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """
    Person model
    """
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    second_last_name = models.CharField(max_length=200, null=True)
    address = models.ForeignKey('app.Address', null=True, on_delete=models.CASCADE)
    phone = models.ForeignKey('app.Phone', null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "person"
