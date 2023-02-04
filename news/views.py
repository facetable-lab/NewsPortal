from django.shortcuts import render, redirect, get_object_or_404

from .models import News, Category
from .forms import AddNewsForm


def index(request):
    news = News.objects.all()

    context = {
        'title': 'Все новости',
        'news': news
    }

    return render(request, template_name='news/index.html', context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = get_object_or_404(Category, pk=category_id)

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


def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)

        if form.is_valid():
            new_object_news = News.objects.create(**form.cleaned_data)
            return redirect(new_object_news)
    else:
        form = AddNewsForm()

    context = {
        'form': form
    }

    return render(request, template_name='news/add_news.html', context=context)
