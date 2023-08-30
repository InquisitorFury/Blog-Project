from django.urls import path

from .views import *

urlpatterns = [
    path("post/", PostList.as_view(), name="post-list"),
    path("post/<str:slug>/<int:month>/<int:year>/", PostDetail.as_view(), name="post-detail"),
    path("post/create/", Postcreate.as_view(), name="post-create"),
    path("post/<str:slug>/<int:month>/<int:year>/update/", Postupdate.as_view(), name="post-update"),
    path("post/<str:slug>/<int:month>/<int:year>/delete/", Postdelete.as_view(), name="post-delete"),
]
