from django.urls import path

from .views import *

urlpatterns = [
    path("tag/", tag_list, name="tag_list"),
    path("tag/<str:slug>", tag_detail, name="tag_detail"),
    path("startup/", startup_list, name="startup_list"),
    path("startup/<str:slug>", startup_detail, name="startup_detail"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>",newslink_detail, name="newslink_detail"),
    path("newslink/",newslink_list , name="newslink_list"),
]
