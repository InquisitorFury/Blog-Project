from rest_framework.fields import(
    CharField,
    IntegerField,
    SlugField,
    DateField,
    EmailField,
    URLField,
)

from rest_framework.serializers import Serializer, HyperlinkedIdentityField, ModelSerializer
from .models import *
class Tagserialiser(ModelSerializer):
    #id = IntegerField(read_only=True) needs to be kept hidden
    #name = CharField(max_length=31)
    #slug = SlugField(max_length=31, read_only=True)
    url = HyperlinkedIdentityField(
        view_name='tagdetail',
        lookup_field = "slug",
    )
    class Meta:
        model = Tag
        fields = "__all__"

class Startupserialser(ModelSerializer):
    #id = IntegerField(read_only=True)
    #name = CharField(max_length=31)
    #slug = SlugField(max_length=31, read_only=True)
    #description = CharField()
    #date_founded = DateField()
    #contact = EmailField()
    #website_link = URLField(max_length=255)
    url = HyperlinkedIdentityField(
        view_name='startupdetail',
        lookup_field = "slug",
    )
    #tags = Tagserialiser(many=True) # many to many field
    class Meta:
        model = Startup
        fields = "__all__"

class NewsLinkSerialiser(ModelSerializer):
   # id = IntegerField(read_only=True)
    #title = CharField(max_length=63)
    #slug = SlugField(max_length=63, read_only=True)
    #date_published = DateField()
    # #article_link = URLField(max_length=255)
    #startups = Startupserialser() #foreignKey or many to one relationship
    class Meta:
        model = newsLink
        fields = "__all__"

