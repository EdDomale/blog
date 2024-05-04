from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.
from .models import Blog, Article
from .forms import BlogForm, ArticleForm

def index(request):
    blogs = Blog.objects.order_by('name')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)

def articles(request, blogId):
    blog = Blog.objects.get(id=blogId)
    articles = blog.article_set.order_by('-dateAdded')
    context = {'blog': blog, 'articles': articles}
    return render(request, 'blogs/articles.html', context)

def article(request, articleId):
    article = Article.objects.get(id=articleId)
    context = {'article': article}
    return render(request, 'blogs/article.html', context)

@login_required
def newBlog(request):
    if request.method != 'POST':
        form = BlogForm()
    else:
        form = BlogForm(data=request.POST)

        if form.is_valid():
            newBlog = form.save(commit=False)
            newBlog.owner = request.user
            newBlog.save()
            return redirect('blogs:index')

    context = {'form': form}
    return render(request, 'blogs/newBlog.html', context)

@login_required
def newArticle(request, blogId):
    blog = Blog.objects.get(id=blogId)

    if request.method != 'POST':
        form = ArticleForm()
    else:
        form = ArticleForm(data=request.POST)

        if form.is_valid():
            newArticle = form.save(commit=False)
            newArticle.blog = blog
            newArticle.save()
            return redirect('blogs:articles', blogId=blogId)

    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/newArticle.html', context)

@login_required
def editArticle(request, articleId):
    article = Article.objects.get(id=articleId)
    blog = article.blog

    checkBlogOwner(request, blog)

    if request.method != 'POST':
        form = ArticleForm(instance=article)
    else:
        form = ArticleForm(instance=article, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:article', articleId=articleId)

    context = {'article': article, 'blog': blog, 'form': form}
    return render(request, 'blogs/editArticle.html', context)

def checkBlogOwner(request, blog):
    if blog.owner != request.user:
        raise Http404