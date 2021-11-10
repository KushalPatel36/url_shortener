from django.urls import path
from . import views

urlpatterns = [
    path('', views.short),
    path('home', views.home),
    path('<str:path>', views.get_full_url),
]