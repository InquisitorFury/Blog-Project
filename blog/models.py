from django.db import models
from datetime import date
# Create your models here.
from organiser.models import Startup, Tag
from django_extensions.db.fields import AutoSlugField

class Post(models.Model):
    """Blog post; news article about startups"""
    title = models.CharField(max_length=63)
    slug = AutoSlugField(
        max_length=63,
        unique=True,
        help_text="A label for URL config",
        populate_from=['title'])
    text = models.TextField()
    pub_date = models.DateField(default=date.today)
    tags = models.ManyToManyField(Tag)
    Startups = models.ManyToManyField(Startup)

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ["-pub_date", 'title']
        verbose_name = "blog post"

    def __str__(self): # refered to as method/behaviours of classes and also called dunders
        date_string = self.pub_date.strftime("%d-%m-%Y")
        return f'{self.title} on {date_string}'
