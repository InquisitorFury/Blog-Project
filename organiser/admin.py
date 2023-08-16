from django.contrib import admin
from .models import  newsLink,Startup,Tag
# Register your models here.
admin.site.register(newsLink)


#customise admin interface
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display =  ("name","slug")

@admin.register(Startup)
class StartupAdmin(admin.ModelAdmin):
    list_display =  ("name","slug")
    #prepopulated_fields = {"slug": ("name",)}

