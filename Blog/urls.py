from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:post_id>', views.details, name='details'),
    path('delete/<int:post_id>', views.delete, name='delete'),
    path('new', views.new, name='new'),
]
