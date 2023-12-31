from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.contrib.auth.decorators import user_passes_test

from gostinitsa.forms import ReservationForm
from gostinitsa.models import Gostinitsa, Room, Reservation
from users.urls import urlpatterns
from users.forms import RegisterUserForm


def index(request):
    return render(request, 'gostinitsa/index.html')


def about(request):
    return render(request, 'gostinitsa/about.html')


def catalog(request):
    gostsinitsi = Gostinitsa.published.all()
    return render(request, 'gostinitsa/shop.html', {'gostinitsi': gostsinitsi})


def thank_you_page(request):
    return render(request, 'gostinitsa/thank_you_page.html')


def show_gostinitsa(request, slug):
    hotel = get_object_or_404(Gostinitsa, slug=slug)
    rooms = Room.objects.filter(hotel=hotel, is_status=Room.Status.AVAILABLE)

    return render(request, 'gostinitsa/gos.html', {'hotel': hotel, 'rooms': rooms})


def show_room(request, hotel_id, room_number):
    hotel = get_object_or_404(Gostinitsa, pk=hotel_id)
    room = get_object_or_404(Room, hotel=hotel, room_number=room_number)

    form = ReservationForm()

    return render(request, 'gostinitsa/room.html', {'hotel': hotel, 'room': room, 'form': form})


def reserve_room(request, hotel_id, room_number):
    hotel = get_object_or_404(Gostinitsa, pk=hotel_id)
    room = get_object_or_404(Room, hotel=hotel, room_number=room_number)

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.room = room

            # Устанавливаем пользователя, выполнившего бронирование
            if request.user.is_authenticated:
                reservation.user = request.user
            else:

                return redirect('users:login')

            reservation.save()

            room.is_status = Room.Status.INREQUEST
            room.save()

            # Редирект на страницу благодарности
            return redirect('thank_you')
        else:
            form = ReservationForm()

        return render(request, 'gostinitsa/room.html', {'hotel': hotel, 'room': room, 'form': form})


@user_passes_test(lambda u: u.is_staff, login_url='users/login')
def operator_requests(request):
    pending_requests = Reservation.objects.filter(status=Reservation.Status.PENDING_APPROVAL)
    return render(request, 'gostinitsa/requests.html', {'requests': pending_requests})


def approve_request(request, request_id):
    reservation = get_object_or_404(Reservation, id=request_id)

    # Обновление информации о бронировании
    reservation.operator_decision = True
    reservation.status = Reservation.Status.CONFIRMED
    reservation.save()

    # Обновление статуса комнаты на 'Занята'
    room = reservation.room
    room.is_status = Room.Status.OCCUPIED
    room.save()

    return redirect('operator_requests')


def reject_request(request, request_id):
    reservation = get_object_or_404(Reservation, id=request_id)

    # Обновление информации о бронировании
    reservation.operator_decision = False
    reservation.status = Reservation.Status.CANCELED
    reservation.save()

    # Обновление статуса комнаты на 'Свободна'
    room = reservation.room
    room.is_status = Room.Status.AVAILABLE
    room.save()
    return redirect('operator_requests')
@user_passes_test(lambda u: u.is_staff, login_url='users/login')
def operator_rooms(request):
    gostinitsy = Gostinitsa.objects.all()
    rooms = Room.objects.all()

    return render(request, 'gostinitsa/operator_rooms.html', {'gostinitsy': gostinitsy, 'rooms': rooms})


@user_passes_test(lambda u: u.is_staff, login_url='users/login')
def requests_page(request):
    requests = Reservation.objects.filter(status=Reservation.Status.PENDING_APPROVAL)
    return render(request, 'gostinitsa/requests.html', {'requests': requests})

def user_requests(request):
    user_requests = Reservation.objects.filter(user=request.user)

    return render(request, 'gostinitsa/user_requests.html', {'user_requests': user_requests})
