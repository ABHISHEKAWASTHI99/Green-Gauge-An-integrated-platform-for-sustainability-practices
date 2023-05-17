from django.shortcuts import render, get_object_or_404
from .models import Article, Tag

def blog_list(request):
    articles = Article.objects.all().order_by('-date')
    tags = Tag.objects.all()
    ctx ={
        'articles': articles,
    }
    return render(request, 'blog/list.html', ctx)

def details(request, user_id):
    article = get_object_or_404(Article, id=user_id)
    ctx = {
        'article': article,
    }
    return render(request, 'blog/details.html', ctx)
