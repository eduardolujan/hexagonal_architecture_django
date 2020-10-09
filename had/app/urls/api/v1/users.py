from django.urls import path, re_path

import had.app.views.api.v1.users as api_users

app_name = "users"

urlpatterns = [
    re_path(
        "users/?",
        api_users.ListUsersApi.as_view(),
        name="list_users"
    ),
    re_path(
        "users/?",
        api_users.CreateUserApi.as_view(),
        name="create_user"
    )
]
