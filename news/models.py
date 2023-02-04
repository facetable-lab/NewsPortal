from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse(viewname='category', kwargs={'category_id': self.pk, })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=97, db_index=True, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, db_index=True, verbose_name='Опубликованно')

    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse(viewname='view_news', kwargs={'news_id': self.pk, })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        ordering = ['-created_at']
