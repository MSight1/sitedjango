from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

from gostinitsa.models import Gostinitsa, Room, Reservation


def index(request):
    return render(request, 'gostinitsa/index.html')
def about(request):
    return render(request,'gostinitsa/about.html')
def catalog(request):
    gostsinitsi = Gostinitsa.published.all()
    return render(request,'gostinitsa/shop.html', {'gostinitsi': gostsinitsi})

def show_gostinitsa(request, slug):
    hotel = get_object_or_404(Gostinitsa, slug=slug)
    rooms = Room.objects.filter(hotel=hotel, is_status=Room.Status.AVAILABLE)

    return render(request, 'gostinitsa/gos.html', {'hotel': hotel, 'rooms': rooms})

@user_passes_test(lambda u: u.is_staff, login_url='users/login')
def requests(request):
    requests = Reservation.objects.all()
    return render(request, 'gostinitsa/requests.html', {'requests': requests})
