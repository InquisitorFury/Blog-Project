from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import ( require_http_methods)
from django.views import View
from .models import *
import json
# Create your views here.
"""
class HelloWorld(View):
    def get(self, request):
        return HttpResponse("Hello world")
"""
class Tag_asdetail(View):
    def get(self, request, pk):
        tag = Tag.objects.get(pk=pk)
        tag_json = json.dumps(
            dict(
                id=tag.pk,
                name = tag.name,
                slug = tag.slug
            )
        )
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