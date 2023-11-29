from django.urls import path, include

from gostinitsa import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:slug>/',views.show_gostinitsa, name='gostinitsa'),
    path('gostinitsa/<int:hotel_id>/room/<int:room_number>/', views.show_room, name='show_room'),
    path('gostinitsa/<int:hotel_id>/room/<int:room_number>/reserve/', views.reserve_room, name='reserve_room'),
    path('operator/requests/', views.operator_requests, name='operator_requests'),
    path('operator/approve/<int:request_id>/', views.approve_request, name='approve_request'),
    path('operator/reject/<int:request_id>/', views.reject_request, name='reject_request'),
    path('operator/rooms/', views.operator_rooms, name='operator_rooms'),
    path('thank-you/', views.thank_you_page, name='thank_you'),
]