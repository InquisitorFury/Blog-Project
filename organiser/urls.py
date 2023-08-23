from django.urls import path

from .views import *

urlpatterns = [
    path("tag/", tag_list, name="tag_list"),
    path("tag/<str:slug>", tag_detail, name="tag_detail"),
    path("startup/", startup_list, name="startup_list"),
    path("startup/<str:slug>", startup_detail, name="startup_detail"),
]
