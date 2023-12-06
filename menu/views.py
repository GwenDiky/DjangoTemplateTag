from django.shortcuts import render
from .templatetags.menu_tags import draw_menu
from django.template import RequestContext

def menu_view(request):
    menu_name = 'main_menu'
    menu_html = draw_menu(menu_name)
    return render(request, 'main.html', {'menu_html': menu_html})

def menu_1(request):
    menu_name = 'main1_menu'
    menu_html = draw_menu(menu_name)
    return render(request, 'menu_1.html', {'menu_html': menu_html})