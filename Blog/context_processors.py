from . import models


def navbar_items(request):
    navbar = models.NavbarItem.objects.order_by('order')
    return {
        'items': navbar
    }


def sidebar_items(request):
    content = models.Post.objects.filter(author=models.BaseUser.objects.get(user=request.user))
    return {
        'content': content
    }
