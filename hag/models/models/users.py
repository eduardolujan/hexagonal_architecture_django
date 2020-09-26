from django.contrib.auth import models
from django.db.models import CharField, UUIDField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class AppUser(models.AbstractUser):
    """Default user for hexagonal_architecture_django."""
    #: First and last name do not cover name patterns around the globe
    class Meta:
        db_table = "app_user"

