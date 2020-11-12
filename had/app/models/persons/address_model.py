from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    """
    Address model
    """
    id = models.UUIDField(primary_key=True, unique=True)
    street = models.CharField(max_length=200)
    interior_number = models.CharField(max_length=200)
    outside_number = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    borough = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    class Meta:
        db_table = "address"
