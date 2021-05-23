from django.contrib import admin

from .models import BaseUser, Post, Page, BlogType, NavbarItem, Folder

models = [BaseUser, Post, Page, BlogType, NavbarItem, Folder]

admin.site.register(models)
