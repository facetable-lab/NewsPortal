from django import forms

from .models import News, Category


# Новая версия формы, связанная с моделью
class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 13}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

# Старая версия формы, не связанная с моделью
# class AddNewsForm(forms.Form):
#     title = forms.CharField(max_length=97, widget=forms.TextInput(
#         attrs={
#             'class': 'form-control'
#         }
#     ), label='Заголовок')
#
#     content = forms.CharField(required=False, widget=forms.Textarea(
#         attrs={
#             'class': 'form-control',
#             'rows': 15
#         }
#     ), label='Текст')
#
#     is_published = forms.BooleanField(required=False, initial=True, label='Опубликовать сразу')
#
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
#         attrs={
#             'class': 'form-control'
#         }
#     ), empty_label='Выберите категорию', label='Категория')
