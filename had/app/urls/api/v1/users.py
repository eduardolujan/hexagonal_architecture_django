from django.urls import path, re_path

import had.app.views.api.v1.users as api_users

app_name = "users"

urlpatterns = [
    re_path(
        "users/?",
        api_users.UserListApi.as_view(),
        name="users"
    )
]
