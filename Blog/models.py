from django.db import models
from django.contrib.auth.models import User


class BaseUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=True)
    second_name = models.CharField(max_length=25, null=True, blank=True, default='')
    first_last_name = models.CharField(max_length=25, null=True, blank=True, default='')
    second_last_name = models.CharField(max_length=25, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name.capitalize()} {self.first_last_name.capitalize()}'


class BlogType(models.Model):
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type


class Post(models.Model):
    author = models.ForeignKey(BaseUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=1200)
    additional_information = models.TextField(max_length=200, null=True, blank=True, default='')
    category = models.ForeignKey(BlogType, on_delete=models.CASCADE, null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.author.first_name}'

    def get_content(self) -> str:
        return self.content if len(self.content) < 300 else f'{self.content[:300]}...'

    def get_title(self) -> str:
        return self.title if len(self.title) < 25 else f'{self.title[:24]}...'

    def update_post(self, title: str, content: str, category: BlogType):
        if title and content and category:
            self.title = title
            self.content = content
            self.category = category
            self.save()


class Page(models.Model):
    name = models.CharField(max_length=15)
    main_header = models.CharField(max_length=30, default='', null=True, blank=True)
    page_title = models.CharField(max_length=20, default='', null=True, blank=True)
    view_name = models.CharField(max_length=15, default='', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_main_header(self):
        return self.main_header


class Logger(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    detail = models.TextField(max_length=5000)
    stack = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.created_at} - {self.name}'


class NavbarItem(models.Model):
    name = models.CharField(max_length=25)
    onclick = models.CharField(max_length=25, default='', null=True, blank=True)
    view = models.CharField(max_length=25, default='', null=True, blank=True)
    order = models.IntegerField()

    def __str__(self):
        return self.name.capitalize()

    def save(self, *args, **kwargs):
        if self.name:
            self.name = self.name.capitalize()
        super(NavbarItem, self).save(*args, **kwargs)
