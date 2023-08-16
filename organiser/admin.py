from django.contrib import admin
from .models import  newsLink,Startup,Tag
# Register your models here.
admin.site.register(newsLink)
admin.site.register(Startup)
admin.site.register(Tag)