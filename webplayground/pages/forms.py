from django import forms
from .models import Page
from django_ckeditor_5.widgets import CKEditor5Widget


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título'}),
            'content': CKEditor5Widget(attrs={"class": "django_ckeditor_5 form-control", 'placeholder': 'Contenido'}),
            'order': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Orden'})
        }
        labels = {
            'title': '',
            'order': '',
            'content': ''
        }
