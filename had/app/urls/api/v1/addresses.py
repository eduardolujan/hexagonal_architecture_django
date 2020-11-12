from django.urls import path, re_path

import had.app.views.api.v1.addresses as api_address

app_name = "app"

urlpatterns = [
    re_path(
        r"^address(/(?P<id>[\w-]+))?/?$",
        api_address.AddressApi.as_view(),
        name="address_api"
    ),
    # re_path(
    #     api_address.ListUsersApi.as_view(),
    #     name="addresses_api"
    # ),
]
