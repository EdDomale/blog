from django import forms
 
from .models import Blog, Article

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description']
        labels = {'name': 'Name', 'description': ''}

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'content']
        labels = {'name': 'Name', 'content': 'Content'}