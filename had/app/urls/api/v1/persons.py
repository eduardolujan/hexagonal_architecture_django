from django.urls import path, re_path

import had.app.views.api.v1.persons as api_users

app_name = "users"

urlpatterns = [
    re_path(
        r"^user(/(?P<_id>[\w-]+))?/?$",
        api_users.UserApi.as_view(),
        name="user_api"
    ),
    re_path(
        r"^users/?$",
        api_users.ListUsersApi.as_view(),
        name="users_api"
    ),
]
