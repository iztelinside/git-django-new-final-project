
from django.urls import path
from . import views

urlpatterns = [

    path("news/", views.news_home, name="news_home"),
    # path("about/", views.about, name="about"),
    # path("contacts/", views.contacts, name="contacts"),
]