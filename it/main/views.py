from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    data = {
        "title": "Eurosport",
        "values": [100, 200, True, "Slogan"],
        "my_list": [10, 20, 30, 40, 50],
        "obj": {
            "name": "Kazakhsport",
            "age": 100,
            "height": 200,

        }
    }
    return render(request, 'main/index.html', data)
# def index(request):
#     return HttpResponse("<h3>We are the champions</h3>")

def about(request):
    return render(request, 'main/about.html', {"title": 'About Page !!!'})
# def about(request):
#     return HttpResponse("<h3>We are the super Codemakers!</h3>")
def contacts(request):
    return render(request, 'main/contacts.html', {"title": 'Contacts Page !!!'})
# Create your views here.


