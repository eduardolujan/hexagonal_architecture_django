from .addresses import urlpatterns as address_urls_patterns
from .persons import urlpatterns as persons_urls_patterns


urlpatterns = []
urlpatterns += address_urls_patterns
urlpatterns += persons_urls_patterns


__all__ = [
    'urlpatterns',
]
