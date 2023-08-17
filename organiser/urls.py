from django.urls import path

from .views import *

urlpatterns = [
    path("", Tag_aslist.as_view(), name="taglist"),
    path("<str:slug>", Tag_asdetail.as_view(), name="tagdetail")
]
