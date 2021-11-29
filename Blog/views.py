from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.utils.html import escape
from django.forms.models import model_to_dict
from .models import Page, Post, User, BaseUser, Logger, BlogType


def index(request: HttpRequest) -> HttpResponse:
    try:
        if request.method != 'GET' or not request.user.is_authenticated:
            return render_4xx(request)
        else:
            context = {
                'page_data': Page.objects.get(name='index'),
                'posts': Post.objects.filter(author=BaseUser.objects.get(user=request.user)).order_by('-id')[:6]
            }
            request.session['location'] = 'index'
            return render(request, 'blog/index.html', context)
    except Exception as PythonException:
        print(PythonException)
        return render_4xx(request)


def posts(request: HttpRequest) -> HttpResponse:
    try:
        if request.method != 'GET':
            return render_4xx(request)
        context = {
            'page_data': Page.objects.get(name='posts'),
            'posts': Post.objects.filter(author=BaseUser.objects.get(user=request.user)).order_by('-id')[:9]
        }
        request.session['location'] = 'posts'
        return render(request, 'blog/posts.html', context)
    except Exception as PythonException:
        print(PythonException)
        return render_4xx(request)


def details(request: HttpRequest, post_id: int):
    context = {
        'page_data': Page.objects.get(name='details'),
        'post': Post.objects.get(pk=post_id)
    }
    request.session['location'] = 'details'
    request.session['post'] = post_id
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
        print(request.POST['content'])
        new_post = Post(
            author=BaseUser.objects.get(user=request.user),
            title=escape(request.POST['title']),
            content=escape(request.POST['content']),
            category=BlogType.objects.get(id=escape(request.POST['category']))
        )
        new_post.save()
        if request.session['location'] == 'details' and request.session['post']:
            return redirect(request.session['location'], request.session['post'])
        return redirect(request.session['location'] if request.session['location'] else 'index')
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
        post.update_post(escape(request.POST['title']), escape(request.POST['content']),
                         BlogType.objects.get(id=escape(request.POST['category'])))
        return redirect('details', post_id)
    else:
        return render_4xx(request)


def search(request: HttpRequest) -> HttpResponse:
    if request.method != 'GET':
        return render_4xx(request, message='Oops! Wrong request!')
    search_input = request.GET.get('s', '')
    if search_input:
        posts_list = Post.objects.filter(title__icontains=search_input)
        if posts_list:
            context = {
                'posts': posts_list,
                'page_data': Page.objects.get(name='search')
            }
            return render(request, 'blog/search.html', context)
        return render_4xx(request, message='No posts found! Try something else!')
    return render_4xx(request, message='Oops! Something went wrong while processing the request, try again.')


def register(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        context = {
            'page_data': Page.objects.get(name='register')
        }
        return render_4xx(request, 'blog/register.phtml', context)
    elif request.method == 'POST':
        # todo: usar un form
        if request.
    else:
        return render_4xx(request, message='Error al ingresar al formulario de registro.')
    new_user = User.objects.create(
        username='test',
        first_name='test1',
        last_name='test2',
        email='test3',
        password='test4'
    )
    new_user.save()
    return JsonResponse({
        'data': model_to_dict(new_user)
    })


def validate_request(request: HttpRequest) -> bool or dict:
    return request.POST['username'] \
           and request.POST['first_name'] \
           and request.POST['last_name'] \
           and request.POST['email'] \
           and request.POST['password']


def login(request: HttpRequest) -> HttpResponse:


# Ajax

def get_posts(request):
    current_posts = int(request.GET.get('current'))
    initial_posts = int(request.GET.get('initial'))
    if request.method == 'GET' and current_posts and initial_posts:
        all_posts = Post.objects.filter(author=BaseUser.objects.get(user=request.user)).order_by('-id')[
                    current_posts:current_posts + initial_posts].values()
        if all_posts:
            return JsonResponse({
                'posts': list(all_posts)
            })
        return JsonResponse({
            'error': 'error'
        })
    return JsonResponse({
        'id': 'test1',
        'title': 'test',
        'content': 'test2',
        'author': 'test3',
        'creation': 'test4'
    })


def render_4xx(request: HttpRequest,
               message: str = 'The request could not be processed, please try again later.') -> HttpResponse:
    return render(request, 'error/4xx_error.html', {'message': message})


def decode_request_body(request_body):
    return decoded_request_to_string(request_body.decode('utf-8'))


def decoded_request_to_string(decoded_request):
    return decoded_request.replace('"', '')
