from django.shortcuts import render
# from django.urls import path
# from . import views
def news_home(request):
    return render(request, 'news/news_home.html')

# urlpatterns = [
#
#     path("", views.index, name="home"),
#     path("about/", views.about, name="about"),
#     path("contacts/", views.contacts, name="contacts"),
#
# ]
# Create your views here.
