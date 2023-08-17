from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import ( require_http_methods)
from django.views import View
from .models import *
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
class Tag_asdetail(View):
    def get(self, request, pk):
       """ tag = Tag.objects.get(pk=pk)
        tag_json = json.dumps(
            dict(
                id=tag.pk,
                name = tag.name,
                slug = tag.slug
            )
        )
        return HttpResponse(tag_json, content_type="application/json")"""
       tag = Tag.objects.get(pk=pk)
       s_tag = Tagserialiser(tag)
       tag_json = render_json(s_tag)
       tag_xml = render_xml(s_tag)
       return HttpResponse(tag_json, content_type="application/json")
    
class Tag_aslist(View):
    def get(self, request):
        tag_list = Tag.objects.all()
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
        return HttpResponse(tag_json, content_type="application/json")