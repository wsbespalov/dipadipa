from django.db import models
from django.db.models import permalink

# Create your models here.

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

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_service_post", None, {"body": self.body})


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
    posted = models.DateField(
        db_index=True,
        auto_now_add=True
    )

    def __unicode__(self):
        return "%s" % self.title

    @permalink
    def get_absolute_url(self):
        return ("view_question_post", None, {"body": self.body})