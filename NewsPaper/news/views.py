from lib2to3.fixes.fix_input import context

from django.http import HttpResponseNotFound

from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    context = {
        'title': 'Главная страница'
    }
    return render(request, 'layout/default.html', context=context)
def new(request):
    posts = Post.objects.all().order_by('-date_time_creation')
    context = {
        'posts': posts,
        'title': 'Список новостей и статей'
    }
    return render(request, 'news/news.html', context=context)
def newid(request, postid):
    post = Post.objects.get(pk=postid)
    context = {
        'post': post,
        'title': 'Новость/статья'
    }
    return render(request, 'news/newid.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена!</h1>')

