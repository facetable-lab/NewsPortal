from django.urls import path

from .views import *

urlpatterns = [
    path(route='', view=HomeNews.as_view(), name='home'),
    path(route='category/<int:category_id>/', view=NewsByCategory.as_view(), name='category'),
    path(route='news/<int:pk>/', view=ViewNews.as_view(), name='view_news'),
    path(route='news/add-news/', view=add_news, name='add_news')
]
