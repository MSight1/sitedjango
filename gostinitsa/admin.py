from django.contrib import admin
from .models import Gostinitsa, Room


# Register your models here.

@admin.register(Gostinitsa)
class GostinitsaAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    ordering = ['time_create','title']
    list_editable = ['is_published']


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'room_number', 'hotel', 'is_status')
    list_display_links = ('id', 'room_number')
    ordering = ['room_number','is_status']
    list_editable = ['is_status', ]