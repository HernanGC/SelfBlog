from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.utils.html import escape
from django.forms.models import model_to_dict
from .models import Page, Post, BaseUser, Logger, BlogType


def index(request: HttpRequest) -> HttpResponse:
    try:
        if request.method != 'GET' or not request.user.is_authenticated:
            return render_4xx(request)
        else:
            context = {}
            page = Page.objects.get(name='index')
            posts = Post.objects.filter(author=BaseUser.objects.get(user=request.user))
            context['posts'] = posts
            context['page_data'] = page
            return render(request, 'blog/index.html', context)
    except Exception as PythonException:
        print(PythonException)
        return render_4xx(request)


def details(request: HttpRequest, post_id: int):
    context = {}
    page = Page.objects.get(name='details')
    post = Post.objects.get(pk=post_id)
    context['post'] = post
    context['page_data'] = page
    return render(request, 'blog/details.html', context)


def new(request) -> HttpResponse:
    if request.method == 'GET':
        context = {
            'page_data': Page.objects.get(name='new'),
            'categories': BlogType.objects.all()
        }
        return render(request, 'blog/new.html', context)
    elif request.method == 'POST':
        if not request.POST['title'] and request.POST['content'] or not request.user.is_authenticated:
            return render_4xx(request)
        print(request.POST)
        new_post = Post(
            author=BaseUser.objects.get(user=request.user),
            title=escape(request.POST['title']),
            content=escape(request.POST['content']),
            category=BlogType.objects.get(id=escape(request.POST['category']))
        )
        new_post.save()
        return redirect('index')
    else:
        return render_4xx(request)


@csrf_protect
def delete(request: HttpRequest, post_id: int) -> JsonResponse:
    if request.method == 'POST' and request.headers['X-Csrftoken'] and 'csrftoken' in request.headers['Cookie']:
        Post.objects.get(pk=post_id).delete()
        return JsonResponse({
            'success': 'true',
            'message': 'The post has been deleted!'
        })
    return JsonResponse({'res': 'YES'})


def edit(request: HttpRequest, post_id: int) -> HttpResponse:
    context = {'page_data': Page.objects.get(name='edit')}
    if request.method == 'GET':
        post = Post.objects.get(id=post_id)
        categories = BlogType.objects.all()
        context['post'] = post
        context['categories'] = categories
        return render(request, 'blog/edit.html', context)
    elif request.method == 'POST':
        if not request.POST['title'] and request.POST['content'] or not request.user.is_authenticated:
            return render_4xx(request)
        post = Post.objects.get(id=post_id)
        if len(request.POST['title']) < 3:
            context['post'] = post
            context['errors'] = {'title': 'Title must be at least 3 characters long.'}
            context['categories'] = BlogType.objects.all()
            return render(request, 'blog/edit.html', context)
        post.update_post(escape(request.POST['title']), escape(request.POST['content']), BlogType.objects.get(id=escape(request.POST['category'])))
        return redirect('details', post_id)
    else:
        return render_4xx(request)


def render_4xx(request: HttpRequest, message: str = 'The request could not be processed, please try again later.') -> HttpResponse:
    return render(request, 'error/4xx_error.html', {'message': message})


def decode_request_body(request_body):
    return decoded_request_to_string(request_body.decode('utf-8'))


def decoded_request_to_string(decoded_request):
    return decoded_request.replace('"', '')
