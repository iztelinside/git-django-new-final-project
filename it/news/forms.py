from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from .models import NewsHome

class NewsHomeForm(ModelForm):
    class Meta:
        model = NewsHome
        fields = ['title', 'anons_content', 'full_content', 'date']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            "anons_content": TextInput(attrs={'class': 'form-control', 'placeholder': 'Anons Content'}),
            "full_content": Textarea(attrs={'class': 'form-control', 'placeholder': 'Full Content'}),
            "date": DateTimeInput(attrs={'class': "datetime", 'placeholder': 'Date'}),
            # 'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название статьи'}),
            # 'anons_content': TextInput(attrs={'class': 'form-control', 'placeholder': 'Анонс статьи'}),
            # 'full_content': TextInput(attrs={'class': 'form-control', 'placeholder': 'Тект статьи'}),
            # 'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата Публикации'})
        }