from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

from .models import News
from .models import Question
from .models import Papers
from .models import Service
from .models import MapObjects
import json
from datetime import datetime
from django.utils import timezone

def index(request):
    return render(
        request=request,
        template_name='index.html',
        context={
            "news": News.objects.all()[:5],
            "papers": Papers.objects.all()[:5]
        }
    )

def news(request):
    return render(
        request=request,
        template_name='news.html',
        context={
            "news": News.objects.all()[:15]
        }
    )
def service(request):
    return render(
        request=request,
        template_name='service.html',
        context={
            "news": News.objects.all()[:5],
            "service": Service.objects.all()[:5]
        }
    )

def map(request):
    return render(
        request=request,
        template_name='map.html',
        context={
            "map": MapObjects.objects.all()[:5]
        }
    )

@csrf_exempt
def get_map_objects(request):
    if request.method == "GET":
        body = list(MapObjects.objects.all()[:5])
        mbody = []
        for b in body:
            mbody.append(b.to_json())
        jbody = {
            "data":mbody
        }
        response = json.dumps(jbody)
        return HttpResponse(
            response
        )

@csrf_exempt 
def map_append_object(request):
    if request.method == 'POST':
        body = request.body
        if isinstance(body, bytes):
            mbody = body.decode("utf-8")
        elif isinstance(body, str):
            pass
        jbody = json.loads(mbody)
        print(jbody)
        # write into database
        mo = MapObjects.objects.create(
            adres = jbody.get("adress"),
            name = jbody.get("name"),
            email = jbody.get("Email"),
            object_name = jbody.get("ObjectName"),
            lng = float(jbody.get("lng")),
            lat = float(jbody.get("lat")),
            date = timezone.make_aware(datetime.now(),timezone.get_default_timezone())
        )
        mo.save()
        return HttpResponse(
            body
        )
    else:
        return HttpResponse(
            "bad request method"
        )

def appeal(request):
    return render(
        request=request,
        template_name='appeal.html',
        context={}
    )

def about(request):
    return render(
        request=request,
        template_name='about.html',
        context={}
    )

def questions(request):
    return render(
        request=request,
        template_name='questions.html',
        context={
            'questions': Question.objects.all()[:5],
             "news": News.objects.all()[:5]
        }
    )
