from django import forms
from .models import Article,Tag

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','slug','body','image','tag',)