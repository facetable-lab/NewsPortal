from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    print(request)
    return HttpResponse('Home news')
