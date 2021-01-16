from django.urls import path, re_path

import had.app.views.api.v1.persons as api_persons

app_name = "app"

urlpatterns = []

urlpatterns = [
    re_path(
        r"^persons(/(?P<id>[\w-]+))?/?$",
        api_persons.PersonApi.as_view(),
        name="user_api"
    )
]
