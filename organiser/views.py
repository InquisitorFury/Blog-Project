from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import ( require_http_methods)
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Tag,newsLink,Startup
import json
# new imports for serialised models
from datetime import date
from pprint import pprint
from xml.dom.minidom import parseString as xml_parse
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from .serialiser import *
# Create your views here.
"""
class HelloWorld(View):
    def get(self, request):
        return HttpResponse("Hello world")
"""

def render_json(serialised_obj):
    """shortcut to make the rendering code easier to read"""
    print(
        JSONRenderer().render(
        serialised_obj.data,
        accepted_media_type="application/json; indent=10",
        ).decode('utf8')
    )

    return JSONRenderer().render(
        serialised_obj.data,
        accepted_media_type="application/json; indent=10",
        ).decode('utf8')

def render_xml(serialised_obj):
    print(
        xml_parse( # python std-lib
            XMLRenderer().render(
                serialised_obj.data,
            )
        
        ).toprettyxml()
    )
    return  xml_parse( # python std-lib
            XMLRenderer().render(
                serialised_obj.data,
            )
        
        ).toprettyxml()


class Tag_asdetail(APIView): # View
    def get(self, request, slug):
        
        #using json.dumps
        """ tag = Tag.objects.get(pk=pk)
        tag_json = json.dumps(
            dict(
                id=tag.pk,
                name = tag.name,
                slug = tag.slug
            )
        )
        return HttpResponse(tag_json, content_type="application/json")"""
       
        # json renderer and http response
        """ 
            tag = Tag.objects.get(pk=pk)
            s_tag = Tagserialiser(tag)
            tag_json = render_json(s_tag)
             tag_xml = render_xml(s_tag)
            return HttpResponse(tag_json, content_type="application/json")
        """
    
        #rest_framework response, it will figure out the type of response on its own whether its json or xml or whatever
        tag = Tag.objects.get(slug=slug)
        s_tag = Tagserialiser(
            tag,
            context={'request':request},
        )

        return Response(s_tag.data)
   
      
    
class Tag_aslist(APIView): # View
    def get(self, request):
        """
        tag_list = Tag.objects.all()
        s_tag_list = Tagserialiser(tag_list,many=True) # for when you're expecting a list of tag objects
         # using json.dumps
         tag_json = json.dumps(
            [
               
                dict(
                    id= tag.pk,
                    name = tag.name,
                    slug = tag.slug
                )
                 for tag in tag_list
            ]
            
        )

        
        #using jsonrenderer

        tag_json = render_json(s_tag_list)
        """
        tag_list = Tag.objects.all()
        s_tag_list = Tagserialiser(tag_list, many=True, context={'request':request})
        return Response(s_tag_list.data)
    

#startup API view
class startupAPIDetail(APIView):
    def get(self,request, slug):
        startup = Startup.objects.get(slug=slug)
        s_startup = Startupserialser(startup, context={'request':request})

        return Response(s_startup.data)
    
class startupAPIList(APIView):
    def get(self, request):
        startup_list = Startup.objects.all()
        s_startup_list = Startupserialser(startup_list, many=True, context={'request':request})

        return Response(s_startup_list.data)


class newslinkAPIDetail(APIView):
    def get(self, request, startup_slug, newslink_slug):
        newslink = newsLink.objects.get(slug=newslink_slug, startups__slug=startup_slug)

        s_newslink = NewsLinkSerialiser(newslink, context={'request':request})

        return Response(s_newslink.data)
    
class newslinkAPIList(APIView):
    def get(self, request):
        newslink = newsLink.objects.all()
        s_newslink = NewsLinkSerialiser(newslink, many=True,context={'request':request})

        return Response(s_newslink.data)
    