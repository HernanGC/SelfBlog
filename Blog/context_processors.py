from . import models


def navbar_items(request):
    navbar = models.NavbarItem.objects.order_by('order')
    return {
        'items': navbar
    }
