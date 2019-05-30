from django.db import models
from django.db.models import permalink
from datetime import datetime
# Create your models here.

from stopmusor import settings

class News(models.Model):
    objects = models.Manager()
    class Meta:
        ordering = ['posted', ]
    title = models.TextField(
        default="New",
        verbose_name="News title"
    )
    slug = models.SlugField(
        max_length=100,
        unique=True
    )
    author = models.TextField(
        default="Author",
        verbose_name="Newws Author"
    )
    body = models.TextField(
        default='Body',
        verbose_name="News body"
    )
    posted = models.DateField(
        db_index=True,
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='media',
        default="image.jpeg"
    )

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_news_post", None, {"slug": self.slug})

class Papers(models.Model):
    objects = models.Manager()
    class Meta:
        ordering = ['posted', ]
    title = models.TextField(
        default="New",
        verbose_name="Papers title"
    )
    foto_title = models.TextField(
        default="New",
        verbose_name="Foto title"
    )
    author = models.TextField(
        default="Author",
        verbose_name="Papers Author"
    )
    body = models.TextField(
        default='Body',
        verbose_name="Papers body"
    )
    posted = models.DateField(
        db_index=True,
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='media',
        default="image.jpeg"
    )

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_papers_post", None, {"body": self.body})

class Service(models.Model):
    objects = models.Manager()
    class Meta:
        ordering = ['posted', ]
    title = models.TextField(
        default="New",
        verbose_name="Service title"
    )
    foto = models.TextField(
        default="Foto",
        verbose_name="Way to foto"
    )
    foto_title = models.TextField(
        default="Foto",
        verbose_name="Foto title"
    )
    author = models.TextField(
        default="Author",
        verbose_name="Service Author"
    )
    body = models.TextField(
        default='Body',
        verbose_name="Service body"
    )
    posted = models.DateField(
        db_index=True,
        auto_now_add=True
    )
    image = models.ImageField(
        upload_to='media',
        default="image.jpeg"
    )

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_service_post", None, {"body": self.body})

class MapObjects(models.Model):
    objects = models.Manager()
    class Meta:
        ordering = ['adres', ]
    adres = models.TextField(
        default="",
        verbose_name="Adres of object"
    )
    name = models.TextField(
        default="",
        verbose_name="Name of user"
    )
    email = models.TextField(
        default="",
        verbose_name="Email of user"
    )
    object_name = models.TextField(
        default="",
        verbose_name="Object name"
    )
    lng = models.FloatField(
        default=0.0
    )
    lat = models.FloatField(
        default=0.0
    )
    date = models.DateTimeField(
        default=datetime.utcnow()
    )
    def __unicode__(self):
        return "%s" % self.object_name

    @permalink
    def get_absolute_url(self):
        return ("view_map_objects", None, {"body": self.adres})

    def to_json(self):
        return dict(
            adress=self.adres,
            name=self.name,
            Email=self.email,
            ObjectName=self.object_name,
            lng=self.lng,
            lat=self.lat,
            # date=self.date
        )

class Question(models.Model):
    objects = models.Manager()
    class Meta:
        ordering = ['posted', ]
    title = models.TextField(
        default="New",
        verbose_name="Question title"
    )
    fio = models.TextField(
        default="",
        verbose_name="Question User Name"
    )
    email = models.TextField(
        default="",
        verbose_name="Question User email"
    )
    body = models.TextField(
        default="",
        verbose_name="Question Body"
    )
    ansver = models.TextField(
        default="",
        verbose_name="Ansver Body"
    )
    posted = models.DateField(
        db_index=True,
        auto_now_add=True
    )

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_question_post", None, {"body": self.body})