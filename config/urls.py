"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from organiser.routers import urlpatterns as organiser_api_urls
from blog.routers import urlpatterns as blog_api_urls
api_urls = blog_api_urls + organiser_api_urls

from organiser import urls as organiser_urls
from blog import urls as blog_urls

from . import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(api_urls)),
    path("", include(organiser_urls)),
    path("", include(blog_urls)),
]
def print_url_pattern_names(patterns):
    """Print a list of urlpattern and their names"""
    for pat in patterns:
        if pat.__class__.__name__ == 'URLResolver':      # load patterns from this URLResolver
            print_url_pattern_names(pat.url_patterns)
        elif pat.__class__.__name__ == 'URLPattern':     # load name from this URLPattern
            if pat.name is not None:
                print('[API-URL] {:>50} -> {}'.format(pat.name, pat.pattern))

if settings.DEBUG:
    print_url_pattern_names(urlpatterns)