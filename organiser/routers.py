from django.urls import path

from .views import *
from .viewssets import TagViewSet

from rest_framework.routers import SimpleRouter
"""
from django.urls import path
from .viewssets import TagViewSet

#manually create url route

tag_create_list = TagViewSet.as_view(
    {"get":"list","post":"create"}

)
tag_retrieve_update_delete = TagViewSet.as_view(
    {
        "get":"retrieve",
        "put":"update",
        "patch":"partial_update",
        "delete":"delete",
    
    }
)

urlpatterns = [
    path("tag/", tag_create_list, name="taglist"), # when using views instead the pattern is path("tag/", tag_aslist, name="taglist")
    path("tag/<str:slug>", tag_retrieve_update_delete, name="tagdetail"), # when using views instead the pattern is path("tag/", tag_asdetail, name="tagdetail")
]

"""

api_router = SimpleRouter()
api_router.register("tag",TagViewSet,basename="tag")
api_routes = api_router.urls

urlpatterns = api_routes +  [
    path("startup/<str:slug>", startupAPIDetail.as_view(), name="startupdetail"),
    path("startup/", startupAPIList.as_view(), name="startuplist"),
    path("newslink/<str:startup_slug>/<str:newslink_slug>", newslinkAPIDetail.as_view(), name="newslinkdetail"),
    path("newslink/", newslinkAPIList.as_view(), name="newslinklist"),
]
