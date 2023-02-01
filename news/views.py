from django.shortcuts import render

from .models import News


def index(request):
    news = News.objects.order_by('-created_at')

    context = {
        'title': 'Список новостей',
        'news': news
    }

    return render(request, template_name='news/index.html', context=context)
