from django.urls import path

from .views import menu_view, menu_1


urlpatterns = [
    path('', menu_view, name='home'),
    path('menu_1', menu_1, name='menu_1'),
]