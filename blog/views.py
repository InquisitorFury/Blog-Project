from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
)

from .models import *
from .serialiser import *

class PostAPIList(ListAPIView):
    """return data for multiple post objects"""
    queryset = Post.objects.all()
    serializer_class = Postserialiser

class PostAPIDetail(RetrieveAPIView):
    """return data for a single post object"""
    queryset = Post.objects.all()
    serializer_class = Postserialiser
    
    def get_object(self):
        """Overide the DRF Method, to include 3 parameters in our URI"""
        month = self.kwargs.get('month') # gets the args in the url
        year = self.kwargs.get('year')
        slug = self.kwargs.get('slug')

        queryset = self.filter_queryset(self.get_queryset)

        post = get_object_or_404( # get this object or return error 404 
            queryset,
            pub_date__year=year, # find the year in the python datetime lib
            pub_date__month=month,# find the month in the python datetime lib
            slug=slug, # find the slug in the post model
        )
        self.check_permissions(self.request, post)
        return post