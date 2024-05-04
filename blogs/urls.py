from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<int:blogId>/', views.articles, name='articles'),
    path('article/<int:articleId>/', views.article, name='article'),
    path('new_blog/', views.newBlog, name='newBlog'),
    path('new_article/<int:blogId>/', views.newArticle, name='newArticle'),
    path('edit_article/<int:articleId>/', views.editArticle, name='editArticle')
]