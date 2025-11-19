from django.shortcuts import render
from .models import NewsHome


def news_home(request):
    news = NewsHome.objects.order_by("title")
    return render(request, 'news/news_home.html', {"news": news})
# from django.urls import path
# from . import views


# urlpatterns = [
#
#     path("", views.index, name="home"),
#     path("about/", views.about, name="about"),
#     path("contacts/", views.contacts, name="contacts"),
#
# ]
# Create your views here.
