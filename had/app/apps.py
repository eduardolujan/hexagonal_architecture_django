from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(AppConfig):
    name = "had.app"
    verbose_name = _("App")

    def ready(self):
        try:
            import had.models.signals  # noqa F401
        except ImportError:
            pass
