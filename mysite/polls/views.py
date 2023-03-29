from django.shortcuts import render
from django.http import HttpResponse


def indeh(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home(request):
    return HttpResponse("Hello, home. You're at the polls index.")


def dom(request):
    return HttpResponse("Hello, Dom. You're at the polls index.")


def index(request):
    template = 'tut.html'
    return render(request, template)
