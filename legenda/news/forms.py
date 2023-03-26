from .models import Aticle
from django.forms import ModelForm, TextInput,DateTimeInput, Textarea


class AticleForm(ModelForm):
    class Meta:
        model=Aticle
        fields = ['title','anons','full_text','date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Название статьи'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Текст статьи'
            }),
        }