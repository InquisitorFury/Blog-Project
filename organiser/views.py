from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import ( require_http_methods)
# Create your views here.

@require_http_methods(["GET","HEAD"])
def hello_world(request):
    return HttpResponse("Hello world")