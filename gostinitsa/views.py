from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'gostinitsa/index.html')
def register(request):
        return render(request,'gostinitsa/registertest.html')
def login(request):
    return render(request,'gostinitsa/login.html')
def about(request):
    return render(request,'gostinitsa/about.html')
