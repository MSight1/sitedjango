from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Gostinitsa, Room, Reservation


@admin.register(Gostinitsa)
class GostinitsaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'time_create', 'is_published', 'link_to_rooms')
    list_display_links = ('title',)
    ordering = ['time_create', 'title']
    list_editable = ['is_published']
    actions = ['set_published', 'set_draft', '']
    search_fields = ['title']
    list_filter = ['is_published']

    @admin.action(description='Опубликовать выбранные гостиницы')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Gostinitsa.Status.PUBLISHED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять с публик. выбранные гостиницы')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Gostinitsa.Status.DRAFT)
        self.message_user(request, f'Изменено {count} записей.')

    def link_to_rooms(self, obj):
        link = reverse('admin:gostinitsa_room_changelist') + f'?hotel__id__exact={obj.id}'
        return format_html('<a href="{}">Список номеров</a>', link)

    link_to_rooms.short_description = 'Список номеров'


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'hotel', 'is_status')
    list_display_links = ('room_number',)
    ordering = ['room_number', 'is_status']
    list_editable = ['is_status', ]
    actions = ['set_aviable', 'set_occupied', ]
    search_fields = ['hotel__title']
    list_filter = ['hotel__title', 'is_status']

    @admin.action(description='Опубликовать выбранные номера')
    def set_aviable(self, request, queryset):
        count = queryset.update(is_status=Room.Status.AVAILABLE)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Снять с публик. выбранные номера')
    def set_occupied(self, request, queryset):
        count = queryset.update(is_status=Room.Status.OCCUPIED)
        self.message_user(request, f'Изменено {count} записей.')

    def show_room_numbers(self, request, queryset):
        selected_rooms = Room.objects.filter(hotel__in=queryset)
        room_numbers = ', '.join(str(room.room_number) for room in selected_rooms)
        self.message_user(request, f'Номера в выбранных гостиницах: {room_numbers}')

    show_room_numbers.short_description = 'Показать номера гостиницы'


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'user', 'room', 'check_in_date', 'duration', 'status', 'booking_date')
    list_display_links = ('id',)
    ordering = ['id', 'check_in_date', 'status']
    list_editable = ['status', ]
    search_fields = ['user__username', 'room__room_number']
    list_filter = ['check_in_date', 'status']

    @admin.action(description='Подтвердить выбранные брони')
    def confirm_reservations(self, request, queryset):
        count = queryset.update(status=Reservation.Status.CONFIRMED)
        self.message_user(request, f'Изменено {count} записей.')

    @admin.action(description='Отменить выбранные брони')
    def cancel_reservations(self, request, queryset):
        count = queryset.update(status=Reservation.Status.CANCELED)
        self.message_user(request, f'Изменено {count} записей.')

    def show_reservation_details(self, request, queryset):
        reservation_details = ', '.join(
            f'ID: {reservation.id}, Пользователь: {reservation.user.username}, Комната: {reservation.room.room_number}, Дата заезда: {reservation.check_in_date}, Продолжительность: {reservation.duration}, Статус: {reservation.status}, Дата бронирования: {reservation.booking_date}'
            for reservation in queryset
        )
        self.message_user(request, f'Детали выбранных броней: {reservation_details}')

    show_reservation_details.short_description = 'Показать детали брони'
