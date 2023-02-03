from django.shortcuts import render, get_object_or_404

from .models import News, Category


def index(request):
    news = News.objects.all()

    context = {
        'title': 'Все новости',
        'news': news
    }

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)

    context = {
        'news': news,
        'current_category': category
    }

    return render(request, template_name='news/category.html', context=context)


def view_news(request, news_id):
    news_item = get_object_or_404(klass=News, pk=news_id)

    context = {
        'news_item': news_item,
    }

    return render(request, template_name='news/view_news.html', context=context)
