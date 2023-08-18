from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer

from .models import Post

from organiser.serialiser import (
    Startupserialser,
    Tagserialiser,
)

class Postserialiser(ModelSerializer):
    tags = Tagserialiser(many=True) # many to many relationship
    Startups = Startupserialser(many=True)

    class Meta:
        model = Post
        fields = "__all__"