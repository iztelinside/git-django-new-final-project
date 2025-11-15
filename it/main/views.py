from django.shortcuts import render
# from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')
# def index(request):
#     return HttpResponse("<h3>We are the champions</h3>")

def about(request):
    return render(request, 'main/about.html')
# def about(request):
#     return HttpResponse("<h3>We are the super Codemakers!</h3>")
# Create your views here.


