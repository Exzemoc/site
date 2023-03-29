from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def str1(request):
    return HttpResponse("page1")


def str2(request):
    return HttpResponse("page 2")


def str3(request):
    return HttpResponse("page 3")
