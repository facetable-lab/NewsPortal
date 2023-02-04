from django import forms

from .models import Category


class AddNewsForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={
            'class': 'form-control'
        }
    ), label='Заголовок')

    content = forms.CharField(required=False, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 15
        }
    ), label='Текст')

    is_published = forms.BooleanField(required=False, initial=True, label='Опубликовать сразу')

    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(
        attrs={
            'class': 'form-control'
        }
    ), empty_label='Выберите категорию', label='Категория')
