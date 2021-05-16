from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Page, Post, BaseUser, Logger
import json
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


def details(request: HttpRequest, post_id: int):
    context = {}
    page = Page.objects.get(name='Details')
    post = Post.objects.get(pk=post_id)
    context['item'] = post
    context['page_data'] = page
    return render(request, 'blog/details.html', context)


def new(request):
    return HttpResponse('OK')

@csrf_protect
def delete(request: HttpRequest, post_id: int):
    if request.method == 'POST' and request.headers['X-Csrftoken'] and 'csrftoken' in request.headers['Cookie']:
        Post.objects.get(pk=post_id).delete()
        print(post_id)
        return JsonResponse({
            'success': 'true',
            'message': 'The post has been deleted!'
        })
    return JsonResponse({'res': 'YES'})


def render_4xx(request: HttpRequest, message: str = 'The request could not be processed, please try again later.') -> HttpResponse:
    return render(request, 'error/4xx_error.html', {'message': message})


def decode_request_body(request_body):
    return decoded_request_to_string(request_body.decode('utf-8'))


def decoded_request_to_string(decoded_request):
    return decoded_request.replace('"', '')
