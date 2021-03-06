from . import models


def navbar_items(request):
    navbar = models.NavbarItem.objects.order_by('order')
    return {
        'items': navbar
    }


def sidebar_items(request):
    content = None
    if request.user.is_authenticated:
        content = models.Post.objects.filter(author=models.BaseUser.objects.get(user=request.user)).order_by('-id')[:10]
    return {
        'content': content
    }
