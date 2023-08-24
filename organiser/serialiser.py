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
    #startups = Startupserialser() #foreignKey or many to one relationship
    class Meta:
        model = newsLink
        fields = "__all__"

