from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "hexagonal_architecture_django.models"
    verbose_name = _("Models")

    def ready(self):
        try:
            import hexagonal_architecture_django.models.signals  # noqa F401
        except ImportError:
            pass
