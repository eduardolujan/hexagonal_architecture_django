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


class Person(models.Model):
    """
    Person model
    """
    id = models.UUIDField(primary_key=True, unique=True)
    name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    second_last_name = models.CharField(max_length=200, null=True)
    address = models.ForeignKey(Address, null=True, on_delete=models.CASCADE)
    phone = models.ForeignKey(Phone, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "person"
