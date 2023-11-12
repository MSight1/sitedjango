from django.shortcuts import render, get_object_or_404

from gostinitsa.models import Gostinitsa, Room


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
