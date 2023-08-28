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

    
class Tagform(ModelForm,LowercaseNameMixin): # modelform calls a validation on the fields such as our slug to stop it being called 
    """HTML forms for Tag objects"""

    class Meta:
        model = Tag
        fields = "__all__"

    
    
    """
    def save(self):
        "Save the data in the bound form"
        return Tag.objects.create(
            name=self.cleaned_data["name"],
            slug=self.cleaned_data["slug"]
        ) 

    """

class StartupForm(
    LowercaseNameMixin, SlugCleanMixin, ModelForm
):
    class Meta:
        model = Startup
        fields = "__all__"