from django.urls import path

from .views import *

urlpatterns = [
    path("blog/", PostList.as_view(), name="post-api-list"),
    path("blog/<str:slug>/<int:month>/<int:year>/", PostDetail.as_view(), name="post-api-list"),
]
