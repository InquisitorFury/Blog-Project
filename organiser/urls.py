from django.urls import path

from .views import *
app_name="organiser"
urlpatterns = [
    path("tag/", tag_list, name="tag_list"),
    path("tag/<str:slug>", tag_detail, name="tag_detail"),
    path("tag/create/", tag_create.as_view(), name="tag_create"),
    path("tag/<str:slug>/update/", tag_update.as_view(), name="tag_update"),
    path("tag/<str:slug>/delete/", tag_delete.as_view(), name="tag_delete"),
    path("startup/", startup_list, name="startup_list"),
    path("startup/<str:slug>", startup_detail.as_view(), name="startup_detail"),
    path("startup/create/", startup_create.as_view(), name="startup_create"),
    path("startup/<str:slug>/update/", startup_update.as_view(), name="startup_update"),
    path("startup/<str:slug>/delete/", startup_delete.as_view(), name="startup_delete"),
]