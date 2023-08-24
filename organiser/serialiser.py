from rest_framework.fields import(
    CharField,
    IntegerField,
    SlugField,
    DateField,
    EmailField,
    URLField,
)
from rest_framework.reverse import reverse
from rest_framework.serializers import (
  Serializer, 
  HyperlinkedIdentityField, 
  ModelSerializer, 
  SerializerMethodField ,
  HyperlinkedRelatedField,
)
from .models import *
class Tagserialiser(ModelSerializer):
    #id = IntegerField(read_only=True) needs to be kept hidden
    #name = CharField(max_length=31)
    #slug = SlugField(max_length=31, read_only=True)
    url = HyperlinkedIdentityField(
        view_name='tag-detail',
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
        view_name='startup-detail',
        lookup_field = "slug",
    )
    tags = Tagserialiser(many=True, read_only=True) # many to many field by having read only it will mean that you can't relate the tags to the startup
    class Meta:
        model = Startup
        fields = "__all__"
    """
     #the startup creation which can now relate to a new tag is done through overriding the create method 
     #however, when updating startup you won't be able to update the tags if it exists in the tags database causing an error

     def create(self, validated_data): # this method is whats called when you use Post and PUT, PATCH on api django restframework
        "create Startup and associate Tags"
        tag_data_list = validated_data.pop("tags") # it gets all the validated data startup and gets the associated tags from the queryset
        startup = Startup.objects.create(**validated_data) # here we modify the startup model in the database using what the user has sent
        #the code below, where we relate bulk-creates objects,
        # works only in databases that return PK after bulk insert
        # which at the time of writing is only PostgreSQL
        tag_list = Tag.objects.bulk_create(
            [Tag(**tag_data) for tag_data in tag_data_list]
        )
        startup.tags.add(*tag_list)
        return startup
    """
   

class NewsLinkSerialiser(ModelSerializer):
   # id = IntegerField(read_only=True)
    #title = CharField(max_length=63)
    #slug = SlugField(max_length=63, read_only=True)
    #date_published = DateField()
    # #article_link = URLField(max_length=255)
    url = SerializerMethodField() # default matches the method name get to the startup 
    startups = HyperlinkedRelatedField(
        queryset = Startup.objects.all(),
        lookup_field = "slug",
        view_name="startup-detail"
    ) #foreignKey or many to one relationship
    class Meta:
        model = newsLink
        exclude = ("id",)

    def get_url(self, newslink):
        """build full URL for NewsLink API detail"""
        relative_url = reverse(
        "newslinkdetail",
        kwargs=dict(
            startup_slug=newslink.startups.slug,
            newslink_slug=newslink.slug,
        )
        )
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(relative_url)
        return relative_url