# users/urls.py

from django.conf.urls import url, include
from users.views import dashboard

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r'^account/', include("django.contrib.auth.urls")),
]