from django.shortcuts import render, redirect
from .models import NewsHome
from .forms import NewsHomeForm


def news_home(request):
    news = NewsHome.objects.order_by('-date')[:5]
    return render(request, 'news/news_home.html', {"news": news})
def create(request):
    error=""
    if request.method == "POST":
        form = NewsHomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error= "Form is not valid"



    form = NewsHomeForm()
    data = {"form": form,
            "error": error}
    return render(request, 'news/create.html', data)
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
