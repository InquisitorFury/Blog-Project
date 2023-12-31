from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.http import require_safe # shortcut, safety method for http methods
from django.views.decorators.http import ( require_http_methods)
from django.urls import reverse_lazy
from django.views import View
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

from django.views.generic import (
     CreateView,
     UpdateView,
     DeleteView,
)
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
#API CREATION 
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
    def put(self, request, slug):
        """Update existing Tag upon PUT

        ALL Tag fields are expected.
        """
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = Tagserialiser(
             tag,
             data = request.data,
             context={"request":request}
        )
        if s_tag.is_valid():
             s_tag.save()
             return Response(
                  s_tag.data, status=HTTP_200_OK
             )
        return Response(
             s_tag.errors,
             status=HTTP_400_BAD_REQUEST
        )
    def patch(self, request, slug):
        """Update existing Tag upon PATCH"""
        tag = get_object_or_404(Tag, slug=slug)
        s_tag = Tagserialiser(
                tag,
                data = request.data,
                context={"request":request}
        )
        if s_tag.is_valid():
                s_tag.save()
                return Response(
                    s_tag.data, status=HTTP_200_OK
                )
        return Response(
                s_tag.errors,
                status=HTTP_400_BAD_REQUEST
        )
    def delete(self,request, slug):
        """DELETE the Tag with specificed slug"""
        tag = get_object_or_404(Tag, slug=slug)
        tag.delete()
        return Response(
            status=HTTP_204_NO_CONTENT
        )
class Tag_aslist(ListCreateAPIView): # View
   #Retrieving API data
   queryset = Tag.objects.all()
   serializer_class = Tagserialiser
"""   def post(self,request):
        "Create new Tag upon Post"
        s_tag = self.serializer_class(
             data = request.data,
             context={"request":request}
        )
        if s_tag.is_valid():
            s_tag.save()
            return Response(
                s_tag.data,
                status=HTTP_201_CREATED
            )
        return Response(
            s_tag.errors, 
            status=HTTP_400_BAD_REQUEST
        )
   """

""" 
   def get(self, request):
        "
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
        "
        tag_list = Tag.objects.all()
        s_tag_list = Tagserialiser(tag_list, many=True, context={'request':request})
        return Response(s_tag_list.data)
    """
    

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

#newslink API view
class newslinkAPIDetail(APIView):
    def get(self, request, startup_slug, newslink_slug):
        newslink = newsLink.objects.get(slug=newslink_slug, startups__slug=startup_slug)

        s_newslink = NewsLinkSerialiser(newslink, context={'request': request})

        return Response(s_newslink.data)
    
class newslinkAPIList(APIView):
    def get(self, request):
        newslink = newsLink.objects.all()
        s_newslink = NewsLinkSerialiser(newslink, many=True,context={'request':request})

        return Response(s_newslink.data)



#html get
@require_safe
def tag_list(request):
        tag_list = Tag.objects.all()
        context = {"tag_list": tag_list}
        return render(request, "tag/list.html", context)
    
@require_safe
def tag_detail(request, slug):
        tag = Tag.objects.get(slug=slug)
        template = loader.get_template("tag/detail.html")
        context = {"tag": tag}
        html_content = template.render(context)
        return render(request, "tag/detail.html", context)

@require_safe
def startup_list(request):
        startup_list = Startup.objects.all()
        context = {"startup_list": startup_list}
        return render(request, "startup/list.html", context)
"""
@require_safe
def startup_detail(request, slug):
        startup = Startup.objects.get(slug=slug)
        context = {"startup": startup, "newslink_create":False}
        return render(request, "startup/detail.html", context)
"""



#forms
from .forms import *

class tag_create(View):
    def get(self, request):
        tagform = Tagform()
        context = {"form":tagform,"update":False}
        return render(request, "tag/form.html", context)
    def post(self,request):
        tagform = Tagform(request.POST)
        
        if tagform.is_valid():
             tag = tagform.save()
             return redirect(tag.get_absolute_url())
        #invalid form
        context = {"form":tagform,"update":False}
        return render(request, "tag/form.html", context)


class tag_update(View):
    def get(self, request,slug):
        tag = get_object_or_404(Tag, slug=slug)
        tagform = Tagform(instance=tag)
        context = {"tag":tag,"form":tagform,"update":True}
        return render(request, "tag/form.html", context)
    def post(self,request,slug):
        tag = get_object_or_404(Tag, slug=slug)
        tagform = Tagform(request.POST,instance=tag) # boundform
        
        if tagform.is_valid():
             tag = tagform.save()
             return redirect(tag.get_absolute_url())
        #invalid form
        context = {"tag":tag,"form":tagform,"update":True}
        return render(request, "tag/form.html", context)

class tag_delete(View):
    def get(self, request,slug):
        tag = get_object_or_404(Tag, slug=slug)
        context = {"tag":tag}
        return render( request, "tag/confirm_delete.html", context)
    def post(self, request,slug):
        tag = get_object_or_404(Tag, slug=slug)
        tag.delete()
        return redirect(reverse("tag_list"))
    
class startup_create(CreateView):
    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update":False}

class startup_update(UpdateView):
    form_class = StartupForm
    model = Startup
    template_name = "startup/form.html"
    extra_context = {"update":True}

class startup_delete(DeleteView):
    model = Startup
    template_name = "startup/confirm_delete.html"
    success_url = reverse_lazy("startup_list")
"""
class newslink_create(CreateView):
    form_class = newslinkForm
    model = newsLink
    template_name = "newslink/form.html"
    extra_context = {"update":False}
    success_url = reverse_lazy("organiser:startup_list")

class newslink_create(UpdateView):
    form_class = newslinkForm
    model = newsLink
    template_name = "newslink/form.html"
    extra_context = {"update":True}
    success_url = reverse_lazy("organiser:startup_list")

class newslink_delete(DeleteView):
    model = newsLink
    template_name = "newslink/confirm_delete.html"
    success_url = reverse_lazy("startup_list")

"""
class startup_detail(View):
    def get(self,request, slug):
        form = newslinkForm()
        startup = Startup.objects.get(slug=slug)
        context = {"startup": startup, "form": form, "newslink_create":True}
        return render(request, "startup/detail.html", context)
    def post(self, request, slug):
        startup = Startup.objects.get(slug=slug)
        form = newslinkForm(request.POST)
        if form.is_valid():
            newslink = form.save()
            redirect(reverse("organiser:startup_detail", kwargs={ "slug":startup.slug}))
        context = {"startup": startup, "form": form, "newslink_create":True}
        return render(request, "startup/detail.html",context)
