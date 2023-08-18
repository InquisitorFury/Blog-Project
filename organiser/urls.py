from django.urls import path

from .views import *

urlpatterns = [
    path("tag/", tag_list, name="taglist"),
    path("tag/<str:slug>", tag_detail, name="tagdetail"),
    path("startup/", startup_list, name="startuplist"),
    path("startup/<str:slug>", startup_detail, name="startupdetail"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>",newslink_detail, name="newslinkdetail"),
    path("newslink/",newslink_list , name="newslinklist"),
]
