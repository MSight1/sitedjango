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
def catalog(request):
    return render(request,'gostinitsa/shop.html')

def show_gostinitsa(request, gos_id):
    return index(request)


gostinitsa_db = [
    {'id':1,'name':'Гостиница ахуенная'},
    {'id':2,'name':'Гостиница пиздатая'},
    {'id':3,'name':'Гостиница крутая'},
]
