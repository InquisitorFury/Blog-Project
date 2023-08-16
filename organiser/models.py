from typing import Type
from django.db import models
from django.db.models.options import Options

# Create your models here.
class Tag(models.Model):
    name = models.CharField(
        max_length=31,
        unique=True)
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text="A label for URL config")
    
    class Meta:
        ordering = ["name"]

    def __str__(self): # refered to as method/behaviours of classes and also called dunders
        return self.name

class Startup(models.Model):
    name = models.CharField(
        max_length=31,
        db_index=True)
    slug = models.SlugField(
        max_length=31,
        db_index=True,
        help_text="A label for URL config")
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
    
class newsLink(models.Model):
    title = models.CharField(
        max_length=31,
        db_index=True)
    slug = models.SlugField(
        max_length=31,
        db_index=True,
        help_text="A label for URL config") 
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



