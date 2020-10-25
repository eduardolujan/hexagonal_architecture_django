from django.conf import settings
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter, SimpleRouter


urlpatterns = []
api_v1_patterns = [
    path("", include("had.app.urls.api.v1.users", namespace="api_v1_users")),
]

api_v1 = []

urlpatterns += api_v1


v1_openapi_schema_view = get_schema_view(
   openapi.Info(
      title="Hexagonal Architecture Django",
      default_version='v1',
      description="Hexagonal Architecture Django"
   ),
   patterns=api_v1,
   public=True,
)


if settings.DEBUG:

    urlpatterns += [
        path(
            f'{settings.URL_PREFIX}documentation/swagger/',
            v1_openapi_schema_view.with_ui('swagger', cache_timeout=0),
            name='schema-swagger-ui'
        ),
        path(
            f'{settings.URL_PREFIX}documentation/',
            v1_openapi_schema_view.with_ui('redoc', cache_timeout=0),
            name='schema-redoc'
        )
    ]

