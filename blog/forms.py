from django.forms import (
    Form,
    CharField,
    SlugField,
    ModelForm,
)
from .models import *
from django.core.exceptions import ValidationError
import re
class LowercaseNameMixin:
    def clean_name(self):
        name  = self.cleaned_data["name"]
        nameregex = re.search("^(create)\w*|^(post)\w*|^(delete)\w*|^(patch)\w*|^(put)\w*", name)
        if nameregex != None:
            raise ValidationError(
                f"slug may not be (create,delete,post,update,patch, put)."
            )
        print(nameregex)
        return name.lower()
    
class SlugCleanMixin: #mixin classs to ensure slug field is not "create"
    """Mixin class to ensure slug field is not 'create' """

    def clean_slug(self):
        print("IN THE SLUG CLEAN MIXIN")
        slug  = self.cleaned_data["slug"]
        if slug == "create".lower():
            raise ValidationError(
                "slug may not be 'create'."
            )
        return slug

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"