from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .models import Page, Post, BaseUser, Logger
import logging
import inspect

# logger = logging.getLogger('Error')


def index(request: HttpRequest) -> HttpResponse:
    try:
        if request.method != 'GET' or not request.user.is_authenticated:
            return render_4xx(request)
        else:
            context = {}
            page = Page.objects.get(name='Index')
            posts = Post.objects.filter(author=BaseUser.objects.get(user=request.user))
            context['posts'] = posts
            context['page_data'] = page
            return render(request, 'blog/index.html', context)
    except Exception as PythonException:
        # log = Logger(PythonException, type(PythonException), PythonException.args, inspect.stack())
        # log.save()
        # logger.exception(PythonException)
        print(PythonException)
        return render_4xx(request)


def render_4xx(request: HttpRequest, message: str = 'The request could not be processed, please try again later.') -> HttpResponse:
    return render(request, '4xx_error.html', {'message': message})
