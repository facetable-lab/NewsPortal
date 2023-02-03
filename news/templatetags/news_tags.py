from django import template

from news.models import Category

register = template.Library()


# inclusion tags могут рендерить шаблон - показывать данные
@register.inclusion_tag('news/show_categories.html')
def show_categories(category_pk=-1):
    categories = Category.objects.all()
    return {
        'categories': categories,
        'current_category': category_pk
    }


# simple tags просто возвращают данные
# @register.simple_tag()  # можно передать имя. name='categories'
# def get_categories():
#     return Category.objects.all()
