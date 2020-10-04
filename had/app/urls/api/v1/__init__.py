from .users import urlpatterns as user_urls_patterns

urlpatterns = []
urlpatterns += user_urls_patterns

__all__ = ('urlpatterns',)
