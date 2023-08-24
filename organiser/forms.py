from django.forms import (
    Form,
    CharField,
    SlugField,
    ModelForm,
)
from .models import *
from django.core.exceptions import ValidationError


class Tagform(ModelForm):
    """HTML forms for Tag objects"""

    name =  CharField(max_length=31)
    slug = SlugField(max_length=31,required=False, help_text="A label for URL config")
    def clean_name(self):
        return self.cleaned_data["name"].lower()
    
    def clean_slug(self):
        slug  = self.cleaned_data["slug"]
        if slug == "create":
            raise ValidationError(
                "slug may not be 'create'."
            )
        return slug
    def save(self):
        """Save the data in the bound form"""
        return Tag.objects.create(
            name=self.cleaned_data["name"],
            slug=self.cleaned_data["slug"]
        )   