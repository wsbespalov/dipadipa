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
        return ("vew_news_post", None, {"slug": self.slug})
