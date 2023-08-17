from rest_framework.fields import(
    CharField,
    IntegerField,
    SlugField,
    DateField,
    EmailField,
    URLField,
)

from rest_framework.serializers import Serializer

class Tagserialiser(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)

class Startupserialser(Serializer):
    id = IntegerField(read_only=True)
    name = CharField(max_length=31)
    slug = SlugField(max_length=31)
    description = CharField()
    date_founded = DateField()
    contact = EmailField()
    website = URLField(max_length=255)
    tags = Tagserialiser(many=True) # many to many field

class NewsLinkSerialiser(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(max_length=63)
    slug = SlugField(max_length=63)
    date_published = DateField()
    article_link = URLField(max_length=255)
    startup = Startupserialser() #foreignKey or many to one relationship
