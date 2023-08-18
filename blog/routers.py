from django.urls import path

from .views import *

urlpatterns = [
   path("blog/", PostAPIList.as_view(), name="post-api-list"),
    path("blog/<str:slug>/<int:month>/<int:year>/", PostAPIList.as_view(), name="post-api-list"),
]
