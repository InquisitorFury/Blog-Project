from django.urls import path

from .views import *

urlpatterns = [
    path("tag/", Tag_aslist.as_view(), name="taglist"),
    path("tag/<str:slug>", Tag_asdetail.as_view(), name="tagdetail"),
    path("startup/<str:slug>", startupAPIDetail.as_view(), name="startupdetail"),
    path("startup/", startupAPIList.as_view(), name="startuplist"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>", newslinkAPIDetail.as_view(), name="newslinkdetail"),
    path("newslink/", newslinkAPIList.as_view(), name="newslinklist"),
]
