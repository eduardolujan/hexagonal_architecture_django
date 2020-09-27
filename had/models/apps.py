from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class HadConfig(AppConfig):
    name = "had.models"
    verbose_name = _("Models")

    def ready(self):
        try:
            import had.models.signals  # noqa F401
        except ImportError:
            pass
