from django.shortcuts import render, get_object_or_404

from gostinitsa.models import Gostinitsa


def index(request):
    return render(request, 'gostinitsa/index.html')
def about(request):
    return render(request,'gostinitsa/about.html')
def catalog(request):
    gostsinitsi = Gostinitsa.objects.all()
    return render(request,'gostinitsa/shop.html', {'gostinitsi': gostsinitsi})

def show_gostinitsa(request, gos_slug):

    gos = get_object_or_404(Gostinitsa, slug=gos_slug)
    data = {
        'title':gos.title,
        'gos':gos,
    }
    return render(request, 'gostinitsa/gos.html', data)
