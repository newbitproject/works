from django.shortcuts import render, redirect, reverse
from . import newbit
from .models import News
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {
    })


# def result(request):
#     test = request.GET.get('q')
#     print(test)
#     return render(request, 'pages/result.html', {
#         'test': test
#     })


def dashboard(request):
    query = request.GET.get('q')
    pie = News.objects.values('cat_selected').annotate(total=Count('cat_selected')).filter(query=query)
    ts = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp').filter(query=query)
    return render(request, 'pages/dashboard.html', {
        'query': query,
        'ts': ts,
        'pie': pie,
    })


#
# def load_df(request):
#     news = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp')
#     return render(request, 'pages/charjs.html', {
#         'news': news,
#     })

def category(request):
    query = request.GET.get('q')
    context = {'query':query}

    return render(request, 'pages/category.html', context)


def topic(request):
    query = request.GET.get('q')
    context = {'query': query}

    return render(request, 'pages/topic.html', context)