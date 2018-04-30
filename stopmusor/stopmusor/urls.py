"""stopmusor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from server import views as server_views

urlpatterns = [
    url(r'^$', server_views.index, name='index'),
    url(r'^news/', server_views.news, name='news'),
    url(r'^service/', server_views.service, name='service'),
    url(r'^map/', server_views.map, name='map'),
    url(r'^appeal/', server_views.appeal, name='appeal'),
    url(r'^about/', server_views.about, name='about'),
    url(r'^questions/', server_views.questions, name='questions'),
    url(r'^admin/', admin.site.urls),
]
