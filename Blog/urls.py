from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts', views.posts, name='posts'),
    path('new', views.new, name='new'),
    path('post/<int:post_id>', views.details, name='details'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('edit/<int:post_id>', views.edit, name='edit'),
    path('search', views.search, name='search'),
    #Ajax
    path('get-posts', views.get_posts, name='get_posts'),
]
