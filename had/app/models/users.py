from django.contrib.auth import models
from django.db import models as dbmodels
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class AppUser(models.AbstractUser):
    REQUIRED_FIELDS = []
    """Default user for had."""
    #: First and last name do not cover name patterns around the globe
    id = dbmodels.UUIDField(primary_key=True)

    class Meta:
        db_table = "app_user"


