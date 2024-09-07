from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page_view(request):
    content_txt = '<h1>This is my home page<h1>'
    return HttpResponse(content_txt)

def about_page_view(request):
    content_txt = '<h1>Welcome to my about page<h1>'
    return HttpResponse(content_txt)
