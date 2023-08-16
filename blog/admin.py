from django.contrib import admin

from .models import Post
# Register your models here.
#admin.site.register(Post)

#customise admin interface
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ("title","slug")