from django.urls import path, re_path

import had.app.views.api.v1.persons as api_persons

app_name = "users"

urlpatterns = []
#
# urlpatterns = [
#     re_path(
#         r"^person(/(?P<id>[\w-]+))?/?$",
#         api_persons.UserApi.as_view(),
#         name="user_api"
#     ),
#     re_path(
#         r"^persons/?$",
#         api_persons.ListUsersApi.as_view(),
#         name="users_api"
#     ),
# ]