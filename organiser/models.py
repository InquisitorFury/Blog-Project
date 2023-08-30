from typing import Type
from django.db import models
from django.db.models.options import Options
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
    name = models.CharField(
        max_length=31,
        unique=True)
    slug = AutoSlugField(
        max_length=31,
        help_text="A label for URL config",
        populate_from=['name'],
        )
    
    class Meta:
        ordering = ["name"]

    def __str__(self): # refered to as method/behaviours of classes and also called dunders
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            "organiser:tag_detail", kwargs={ "slug": self.slug}
        )
class Startup(models.Model):
    name = models.CharField(
        max_length=31,
        db_index=True)
    slug = AutoSlugField(
        max_length=31,
        db_index=True,
        help_text="A label for URL config",
        populate_from=['name'])
    description = models.TextField()
    date_founded = models.DateField()
    contact = models.EmailField()
    website_link = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        get_latest_by  = 'date_founded'
        ordering = ["name"]
        
    def __str__(self): # refered to as method/behaviours of classes and also called dunders
        return self.name
    def get_absolute_url(self):
        return reverse(
            "organiser:startup_detail", kwargs={ "slug":self.slug}
        )
    
class newsLink(models.Model):
    title = models.CharField(
        max_length=31,
        db_index=True)
    slug = AutoSlugField(
        max_length=31,
        db_index=True,
        help_text="A label for URL config",
        populate_from=['title']) 
    date_published = models.DateField()
    article_link = models.URLField()

    startups = models.ForeignKey(Startup, on_delete=models.CASCADE)

    class Meta:
        get_latest_by = 'date_published'
        ordering = ["-date_published"]
        unique_together = ('slug','startups')
        verbose_name = 'news article'

    def __str__(self): # refered to as method/behaviours of classes and also called dunders
        return f'{self.startups}: {self.title}'



