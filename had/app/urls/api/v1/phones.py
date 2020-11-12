

from django.urls import path, re_path

# ApiViews
import had.app.views.api.v1.phones as phone_api

app_name = "app"

urlpatterns = [
    re_path(
        r"^phone(/(?P<id>[\w-]+))?/?$",
        phone_api.PhoneApi.as_view(),
        name="phone_api"
    ),
    # re_path(
    #     api_address.ListUsersApi.as_view(),
    #     name="addresses_api"
    # ),
]
