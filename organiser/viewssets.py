from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_safe # shortcut, safety method for http methods
from django.views.decorators.http import ( require_http_methods)
from rest_framework.decorators import action
from django.views import View
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import (
     HTTP_201_CREATED,
     HTTP_400_BAD_REQUEST,
     HTTP_200_OK,
     HTTP_204_NO_CONTENT,
)

from rest_framework.generics import(
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
)
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from .models import Tag,newsLink,Startup
import json
# new imports for serialised models
from datetime import date
from pprint import pprint
from xml.dom.minidom import parseString as xml_parse
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from .serialiser import *

#Tag API view set
class TagViewSet(ModelViewSet): #viewset has actions as your methods over http methods like put,patch..
    """A set of views for the Tag model"""
    """
    manually using viewsets using action methods
 
    def list(self, request):
        "List Tag objects"
        tag_list = Tag.objects.all()
        s_tag = Tagserialiser(
            tag_list,
            many=True,
            context={"request":request}
        )
        return Response(s_tag.data)
    
    def retrieve(self, request, slug):
        tag = Tag.objects.get(slug=slug)
        s_tag = Tagserialiser(
            tag,
            context={'request':request},
        )

        return Response(s_tag.data)
    def create(self,request):
        "Create a new Tag object"
        s_tag = Tagserialiser(
            data=request.data,
            context={"request":request}
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(s_tag.data, status=HTTP_201_CREATED)
        return Response(
            s_tag.errors,
            status=HTTP_400_BAD_REQUEST
        )
    def update(self,request,slug):
        "Update an existing Tag object"
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = Tagserialiser(
            tag,
            data = request.data,
            context={"request":request},
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(s_tag.data, status=HTTP_201_CREATED)
        return Response(
            s_tag.errors,
            status=HTTP_400_BAD_REQUEST
        )
    def partial_update(self,request,slug):
        "Update an existing Tag object partially"
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = Tagserialiser(
            tag,
            data = request.data,
            partial=True,
            context={"request":request},
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(s_tag.data, status=HTTP_201_CREATED)
        return Response(
            s_tag.errors,
            status=HTTP_400_BAD_REQUEST
        )
    def delete(self,request, slug):
        "DELETE the Tag with specificed slug"
        tag = get_object_or_404(Tag, slug=slug)
        tag.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )
    """

    lookup_field = "slug"
    queryset = Tag.objects.all()
    serializer_class = Tagserialiser


class StartupViewSet(ModelViewSet):
    """A set of views for the Startup model"""
    lookup_field = "slug"
    queryset = Startup.objects.all()
    serializer_class = Startupserialser
    
    #this block will allow for tags to be added to the startup
    @action(detail=True, methods=["HEAD","GET","POST"])
    def tags(self,request, slug=None):
        """Relate a POSTED Tag to Startup in URI"""        
        startup = self.get_object()
        if request.method in ("HEAD", "GET"):
            s_tag = Tagserialiser(
                startup.tags,
                many=True,
                context = {"request":request}
            )
            return Response(s_tag.data)
        tag_slug = request.data.get("slug")
        if not tag_slug:
            return Response(
                "Slug of tag must be specified",
                status=HTTP_400_BAD_REQUEST,
            )
        tag = get_object_or_404(Tag, slug__iexact=tag_slug)
        startup.tags.add(tag)
        return Response(
            status=HTTP_204_NO_CONTENT
        )