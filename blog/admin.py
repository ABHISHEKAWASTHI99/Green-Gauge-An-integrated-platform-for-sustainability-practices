from django.contrib import admin
from .models import Article, Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)  

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'title', 'slug', 'body', 'date', 'author', 'image')


