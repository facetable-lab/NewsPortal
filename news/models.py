from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Изображение')
    is_published = models.BooleanField(default=False, verbose_name='Опубликованно')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

        ordering = ['-created_at']
