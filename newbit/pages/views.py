from django.shortcuts import render
from . import newbit
from .models import News
from django.db.models import Count

# Create your views here.
def index(request):
    return render(request, 'pages/index.html', {
    })


def result(request):
    test = request.GET.get('q')
    print(test)
    return render(request, 'pages/result.html', {
        'test': test
    })


def load_df(request):
    news = News.objects.values('date').annotate(total=Count('date')).order_by('date_tmp')
    return render(request, 'pages/charjs.html', {
        'news': news,
    })

