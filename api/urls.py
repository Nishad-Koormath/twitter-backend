from django.urls import path
from .views import get_comments, hide_red_flags

urlpatterns = [
    path("comments/", get_comments),
    path("hide-red-flags/", hide_red_flags),
]
