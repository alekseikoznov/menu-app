from django import template
from menu.models import MenuItem
from django.urls import resolve

register = template.Library()


@register.inclusion_tag('menu_app/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_path = context['request'].path
    current_url_name = resolve(current_path).url_name
    menu_items = MenuItem.objects.filter(menu__name=menu_name, parent=None)

    def is_active(url):
        return (current_path.startswith(url)
                or current_url_name == resolve(url).url_name)

    return {
        'menu_items': menu_items,
        'current_path': current_path,
        'is_active': is_active
    }
