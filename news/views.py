from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import News, Category
from .forms import AddNewsForm


class HomeNews(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/index.html'

    # extra_context = {'title': 'Все новости'}

    def get_queryset(self):
        return News.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Все новости'
        return context


class NewsByCategory(ListView):
    model = News
    context_object_name = 'news'
    template_name = 'news/category.html'

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_category'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'
    template_name = 'news/view_news.html'


def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST)

        if form.is_valid():
            # Для старой формы
            # new_object_news = News.objects.create(**form.cleaned_data)
            new_object_news = form.save()
            return redirect(new_object_news)
    else:
        form = AddNewsForm()

    context = {
        'form': form
    }

    return render(request, template_name='news/add_news.html', context=context)
