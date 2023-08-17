from django.urls import path

from .views import *

urlpatterns = [
    path("", HelloWorld.as_view(), name="hello"),
]
