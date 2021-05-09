from django.contrib import admin

from .models import BaseUser, Post, Page, BlogType, NavbarItem

models = [BaseUser, Post, Page, BlogType, NavbarItem]

admin.site.register(models)
