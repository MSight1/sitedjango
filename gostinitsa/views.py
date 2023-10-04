from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('Страница приложения гостиница')
def register(request):
    return HttpResponse('Страница приложения гостиница')
def login(request):
    return HttpResponse('Страница приложения гостиница')
def about(request):
    return HttpResponse('Страница приложения гостиница')