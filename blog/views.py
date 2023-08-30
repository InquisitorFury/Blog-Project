from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework.generics import(
    ListAPIView,
    RetrieveAPIView,
)
from django.views import (
    View
)
from django.views.generic import (
     CreateView,
     UpdateView,
     DeleteView,
)
from .forms import *
from django.views.generic import ListView
from .models import *
from .serialiser import *
from django.urls import reverse, reverse_lazy
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
class PostList(ListView):
    model = Post
    template_name = "post/list.html"

class PostDetail(View):
    def get(self, request,year,month,slug):
        post = get_object_or_404(
            Post,
            pub_date__year=year,
            pub_date__month=month,
            slug=slug
        )
        context = {"post":post}
        return render(request, "post/detail.html",context)
    
class Postcreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = "post/form.html"
    extra_context = {"update":False}

class Postupdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = "post/form.html"
    extra_context = {"update":True}

class Postdelete(DeleteView):
    model = Post
    template_name = "post/confirm_delete.html"
    success_url = reverse_lazy("post_list")