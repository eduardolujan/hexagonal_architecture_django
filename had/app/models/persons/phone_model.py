from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Phone(models.Model):
    """
    Phone model
    """
    id = models.UUIDField(primary_key=True, unique=True)
    number = models.CharField(max_length=200)
    extension = models.CharField(max_length=200)

    class Meta:
        db_table = "phone"
