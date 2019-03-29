from django.contrib import admin

# Register your models here.

from server.models import News
from server.models import Papers
from server.models import Service
from server.models import MapObjects
from server.models import Question

admin.autodiscover()
admin.site.register(News)
admin.site.register(Papers)
admin.site.register(Service)
admin.site.register(MapObjects)
admin.site.register(Question)
