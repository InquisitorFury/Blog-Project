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
        month = self.kwargs.get('month')
        year = self.kwargs.get('year')
        slug = self.kwargs.get('slug')

        queryset = self.filter_queryset(self.get_queryset)

        post = get_object_or_404(
            queryset,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug,
        )
        self.check_permissions(self.request, post)
        return post