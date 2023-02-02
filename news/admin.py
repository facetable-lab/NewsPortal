from django.contrib import admin

from .models import News, Category


class NewsAdmin(admin.ModelAdmin):
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')
    list_display = ('pk', 'title', 'category', 'created_at', 'updated_at', 'is_published')
    list_display_links = ('pk', 'title', 'category')
    search_fields = ('title', 'content')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'pk')
    list_display_links = ('title', 'pk')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
