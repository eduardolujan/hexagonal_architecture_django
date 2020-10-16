from django.urls import path, re_path

import had.app.views.api.v1.users as api_users

app_name = "users"

urlpatterns = [
    re_path(
        r"^user/(?P<id>[\w-]+)/?$",
        api_users.GetUserApi.as_view(),
        name="get_user"
    ),
    re_path(
        r"^user/?$",
        api_users.CreateUserApi.as_view(),
        name="create_user"
    ),
    re_path(
        r"^users/?$",
        api_users.ListUsersApi.as_view(),
        name="list_users"
    ),
]
