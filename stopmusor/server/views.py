from django.shortcuts import render, render_to_response, get_object_or_404

from django.http import HttpResponse

# Create your views here.

from .models import News
from .models import Question
from .models import Papers
from .models import Service

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
            "news": News.objects.all()[:5]
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
            "map": News.objects.all()[:5]
        }
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